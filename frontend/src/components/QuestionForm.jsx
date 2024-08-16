import { useState } from "react";
import axios from "axios";
import ChatHistory from "./ChatHistory";
import InputForm from "./InputForm";

const api = axios.create({
  baseURL: "https://expert-acorn-wvr6p5q4vgrhq9g-8000.app.github.dev",
});

function QuestionForm() {
  const [chatHistory, setChatHistory] = useState([]);

  const handleQuestionSubmit = async (question) => {
    // Add the question to the chat history
    setChatHistory([...chatHistory, { type: "question", text: question }]);
  
    // Send the question to the API
    const response = await api.post("/chat", { message: question });
  
    // Add the response to the chat history with the tools used
    setChatHistory((prevHistory) => [
      ...prevHistory,
      {
        type: "response",
        text: response.data.answer,
        toolsUsed: response.data.tools_used, // Add the tools used to the chat history
      },
    ]);
  };

  return (
    <div
      style={{
        maxWidth: "600px",
        margin: "0 auto",
        padding: "10px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <ChatHistory chatHistory={chatHistory} />
      <InputForm onSubmit={handleQuestionSubmit} />
    </div>
  );
}

export default QuestionForm;
