from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.chatlogic import get_answer
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Chatbot API",
    description="API for a simple chatbot",
    version="0.1",
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    # allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat", description="Chat with the chatbot")
def chat(message: Message):
    response = get_answer(message)
    response_content = {
        "question": message.message,
        "answer": response["answer"],
    }

    return JSONResponse(content=response_content, status_code=200)
