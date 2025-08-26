# PubMed Medical Doubts Search App

A simple web-based tool for compiling medical-related questions and retrieving abstracts from PubMed using the official Entrez API.

## Features
- Search by medical question or keyword.
- Fetches the top PubMed abstract for each query.
- Simple HTML/CSS frontend.
- FastAPI Python backend, easily extendable.

## Usage
1. **Backend**: Run `main.py` using FastAPI
    ```
    pip install fastapi uvicorn requests
    uvicorn main:app --reload
    ```
2. **Frontend**: Open `index.html` in your browser.

## Contribute
- Suggestions, issues, and PRs are welcome.
- Extend by adding AI-powered explanations or caching.

## Disclaimer
This app provides medical literature abstracts for informational purposes only. It does **not** replace professional medical advice.
