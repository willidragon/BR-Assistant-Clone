# app.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
# from src.chatlogic import get_answer
from src.chatlogic_modify import get_answer
import logging


app = FastAPI(
    title="Chatbot API",
    description="API for a simple chatbot",
    version="0.1",
)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Log the origin of incoming requests
@app.middleware("http")
async def log_origin(request: Request, call_next):
    origin = request.headers.get("origin")
    logging.info(f"Request origin: {origin}")
    response = await call_next(request)
    return response

# origins = [
#     "http://localhost:3000",
#     "http://127.0.0.1:8000"
#     # Add other origins here as you identify them
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class Message(BaseModel):
    message: str

@app.post("/chat", description="Chat with the chatbot")
def chat(message: Message):
    response = get_answer(message.message)  # Use message.message to get the string input
    response_content = {
        "input": message.message,
        "answer": response["answer"],
        "tools_used": response["tools_used"],
    }

    return JSONResponse(content=response_content, status_code=200)
