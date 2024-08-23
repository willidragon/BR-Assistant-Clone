
# BR Assistant ChatBot

This project includes both frontend and backend services. The frontend is built with React, and the backend uses FastAPI. DB is built with Postgres, and can be started with docker.

## Directory Structure

```plaintext
.
|__ .devcontainer/
|   |__ devcontainer.json
|
|__ backend/
|   |__ .env
|   |__ Pipfile
|   |__ poetry.lock
|   |__ pyproject.toml
|   |__ README.md
|   |__ src/
|       |__ __pycache__/
|       |__ app.py
|       |__ chatlogic.py
|       |__ custom_tools.py
|       |__ files/
|           |__ recipe.csv
|
|__ frontend/
|   |__ .gitignore
|   |__ package.json
|   |__ public/
|   |   |__ index.html
|   |   |__ manifest.json
|   |   |__ robots.txt
|   |__ README.md
|   |__ src/
|       |__ App.css
|       |__ App.js
|       |__ App.test.js
|       |__ components/
|       |   |__ ...
|       |__ index.css
|       |__ index.js
|       |__ reportWebVitals.js
|       |__ setupTests.js
|
|__ mpcs_database_mock/
|   |__ docker-compose.yml
|   |__ fetch.py
|   |__ populate_table.py
|   |__ recipe.csv
|   |__ schema.sql
```

## Setup Instructions

### Backend
> Make sure to cd to the backend folder for the following operations

1. **Install Dependencies:**
   - Ensure [Poetry](https://python-poetry.org/) is installed.
   - Run `poetry install` to install the required packages.

2. **Environment Configuration:**
   - Replace the placeholders in the `.env` file with the correct environment variables. Ensure all necessary values are properly configured.
    
    **.env**\
    `OPENAI_API_KEY=insert key here`

3. **Run the Backend:**
   - Use the command `uvicorn src.app:app --reload` inside the backend folder to start the FastAPI server. 

### Frontend
> Make sure to cd to the frontend folder for the following operations

1. **Install Dependencies:**
   - Ensure [Node.js](https://nodejs.org/) and npm are installed.
   - Navigate to the `frontend/` directory and run `npm install`.

2. **Run the Frontend:**
   - In the `frontend/` directory, run `npm start` to start the React development server.

### DB

1. 確保已安裝 [Docker](https://www.docker.com/)。
2. 在 [`mpcs_database_mock`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2Fcodespaces-blank%2Fmpcs_database_mock%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/workspaces/codespaces-blank/mpcs_database_mock") 目錄下運行以下命令啟動資料庫服務：

```bash
docker-compose up -d
```

3. if the container already exists, run
```
docker start mpcs_postgres
```


## Project Overview

### Backend

- **`src/app.py`:** The main FastAPI application file.
- **`src/chatlogic.py`:** Module handling the chat logic.The main component of the Langchain logic is written here.
- **`src/custom_tools.py`:** Custom tools and utilities for Langchain is written here.

### Frontend

- **`src/App.js`:** Main React component.
- **`src/components/`:** Folder containing various React components.

### Database Mock (mpcs_database_mock)

- **`docker-compose.yml`:** Docker configuration for spinning up the mock database.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
