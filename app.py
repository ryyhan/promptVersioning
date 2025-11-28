import streamlit as st
from database import init_db, get_db, Prompt, PromptVersion
from sqlalchemy.orm import Session
import datetime

# Initialize DB
init_db()

st.set_page_config(page_title="Prompt Versioning", layout="wide")

def get_session():
    return next(get_db())

session = get_session()

st.title("Prompt Versioning App")

# Sidebar
st.sidebar.header("Prompts")
if st.sidebar.button("New Prompt"):
    st.session_state.selected_prompt_id = None

prompts = session.query(Prompt).all()
for p in prompts:
    if st.sidebar.button(p.name, key=f"prompt_{p.id}"):
        st.session_state.selected_prompt_id = p.id

# Main Content
if "selected_prompt_id" not in st.session_state or st.session_state.selected_prompt_id is None:
    st.header("Create New Prompt")
    new_name = st.text_input("Prompt Name")
    if st.button("Create"):
        if new_name:
            new_prompt = Prompt(name=new_name)
            session.add(new_prompt)
            session.commit()
            st.success(f"Created {new_name}")
            st.rerun()
else:
    prompt = session.query(Prompt).filter(Prompt.id == st.session_state.selected_prompt_id).first()
    if not prompt:
        st.error("Prompt not found")
        st.stop()

    st.header(f"Prompt: {prompt.name}")

    tab1, tab2 = st.tabs(["Edit", "History"])

    with tab1:
        # Get latest version content
        latest_version = session.query(PromptVersion).filter(PromptVersion.prompt_id == prompt.id).order_by(PromptVersion.version_number.desc()).first()
        default_content = latest_version.content if latest_version else ""
        
        new_content = st.text_area("Content", value=default_content, height=400)
        comment = st.text_input("Version Comment")
        
        if st.button("Save New Version"):
            if new_content:
                # Determine version number
                next_version = (latest_version.version_number + 1) if latest_version else 1
                
                version = PromptVersion(
                    prompt_id=prompt.id,
                    version_number=next_version,
                    content=new_content,
                    comment=comment
                )
                session.add(version)
                session.commit()
                st.success(f"Saved Version {next_version}")
                st.rerun()

    with tab2:
        versions = session.query(PromptVersion).filter(PromptVersion.prompt_id == prompt.id).order_by(PromptVersion.version_number.desc()).all()
        for v in versions:
            with st.expander(f"v{v.version_number} - {v.created_at.strftime('%Y-%m-%d %H:%M')} - {v.comment}"):
                st.code(v.content)
