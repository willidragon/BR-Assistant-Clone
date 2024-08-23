import { useState } from "react";
import axios from "axios";
import ChatHistory from "./ChatHistory";
import InputForm from "./InputForm";

// Load the base URL from environment variables
const api = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL,
});

function QuestionForm() {
  const [chatHistory, setChatHistory] = useState([]);

  const handleQuestionSubmit = async (question) => {
    // Add the question to the chat history
    setChatHistory([...chatHistory, { type: "question", text: question }]);
  
    try {
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
    } catch (error) {
      // Handle the error here
      console.error("Network error occurred:", error);
  
      // Optionally, you can display a user-friendly message in the chat history
      setChatHistory((prevHistory) => [
        ...prevHistory,
        {
          type: "response",
          text: "Unable to reach the server. Please try again later.",
          toolsUsed: "No tools used", // You can adjust this based on your needs
        },
      ]);
    }
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
