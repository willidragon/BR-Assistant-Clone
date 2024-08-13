# Backend

This is the backend service project directory.

## Environment Setup

1. Ensure you have [Poetry](https://python-poetry.org/) installed.
2. Copy the `.env` file and fill in the necessary environment variables.

## Starting the Service

Use `uvicorn` to start the backend service:

```bash
poetry run uvicorn src.app:app --reload
```

This command will start the FastAPI application located in `src/app.py` with auto-reload enabled.

## Project Structure

```
backend/
├── .env                    # Environment variables
├── poetry.lock             # Poetry lock file
├── pyproject.toml          # Project configuration
├── README.md               # Project documentation
└── src/
    ├── __init__.py         # Makes src a package
    ├── app.py              # Main FastAPI application
    └── chatlogic.py        # Module handling chat logic
```

- **`src/app.py`**: The main FastAPI application.
- **`src/chatlogic.py`**: Module that handles chat logic.
