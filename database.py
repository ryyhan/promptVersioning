import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Prompt(Base):
    __tablename__ = 'prompts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    versions = relationship("PromptVersion", back_populates="prompt", cascade="all, delete-orphan")

class PromptVersion(Base):
    __tablename__ = 'prompt_versions'
    id = Column(Integer, primary_key=True)
    prompt_id = Column(Integer, ForeignKey('prompts.id'), nullable=False)
    version_number = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    prompt = relationship("Prompt", back_populates="versions")

DATABASE_URL = "sqlite:///prompts.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
