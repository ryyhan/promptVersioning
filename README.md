# Prompt Versioning App

A simple and efficient Streamlit application for managing and versioning text prompts. This tool allows you to create prompts, save multiple versions, and track the history of your changes, making it easier to iterate on your prompt engineering.

## Features

-   **Create Prompts**: Easily create named prompts to organize your work.
-   **Version Control**: Automatically version your prompts every time you save.
-   **History Tracking**: View a complete history of all versions for a specific prompt.
-   **Comments**: Add comments to each version to document changes or results.
-   **Local Storage**: Uses SQLite for persistent, serverless local storage.

## Prerequisites

-   Python 3.8+
-   `pip` (Python package installer)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ryyhan/promptVersioning.git
    cd promptVersioning
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2.  The app will open in your default web browser (usually at `http://localhost:8501`).

3.  **To create a new prompt**:
    -   Click the "New Prompt" button in the sidebar.
    -   Enter a name and click "Create".

4.  **To edit and version a prompt**:
    -   Select a prompt from the sidebar.
    -   Edit the content in the "Edit" tab.
    -   Add a comment describing your changes.
    -   Click "Save New Version".

5.  **To view history**:
    -   Switch to the "History" tab to see past versions.