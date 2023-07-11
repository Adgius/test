@echo off

call .venv\Scripts\activate

uvicorn start:app --reload
pause