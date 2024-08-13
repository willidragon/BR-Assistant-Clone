from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.chatlogic import get_answer

app = FastAPI(
    title="Chatbot API",
    description="API for a simple chatbot",
    version="0.1",
)

@app.post("/chat", description="Chat with the chatbot")
def chat(message: str):
    response = get_answer(message)
    response_content = {
        "question": message,
        "answer": response["answer"],
    }

    return JSONResponse(content=response_content, status_code=200)
