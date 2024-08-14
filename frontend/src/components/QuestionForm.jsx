import { useState } from "react";
import axios from "axios";

const api = axios.create({
  baseURL: "https://expert-acorn-wvr6p5q4vgrhq9g-8000.app.github.dev",
});

function QuestionForm() {
  const [question, setQuestion] = useState(""); // Correct way to destructure useState
  const [chatHistory, setChatHistory] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (question.trim() === "") return;

    // Add the question to the chat history
    setChatHistory([...chatHistory, { type: "question", text: question }]);

    // Send the question to the API
    const response = await api.post("/chat", { message: question });
    
    // Add the response to the chat history
    setChatHistory((prevHistory) => [
      ...prevHistory,
      { type: "response", text: response.data.answer },
    ]);

    // Clear the input field
    setQuestion("");
  };

  return (
    <div style={{ maxWidth: "600px", margin: "0 auto", padding: "10px", fontFamily: "Arial, sans-serif" }}>
      <div style={{ border: "1px solid #ccc", borderRadius: "8px", padding: "10px", height: "400px", overflowY: "auto", backgroundColor: "#f9f9f9" }}>
        {chatHistory.map((entry, index) => (
          <div
            key={index}
            style={{
              marginBottom: "10px",
              textAlign: entry.type === "question" ? "right" : "left",
            }}
          >
            <div
              style={{
                display: "inline-block",
                padding: "10px",
                borderRadius: "8px",
                backgroundColor: entry.type === "question" ? "#0084ff" : "#e4e6eb",
                color: entry.type === "question" ? "#fff" : "#000",
              }}
            >
              {entry.text}
            </div>
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit} style={{ display: "flex", marginTop: "10px" }}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          style={{
            flex: "1",
            padding: "10px",
            borderRadius: "8px",
            border: "1px solid #ccc",
          }}
          placeholder="Type your question..."
        />
        <button
          type="submit"
          style={{
            marginLeft: "10px",
            padding: "10px 20px",
            borderRadius: "8px",
            border: "none",
            backgroundColor: "#0084ff",
            color: "#fff",
            cursor: "pointer",
          }}
        >
          Send
        </button>
      </form>
    </div>
  );
}

export default QuestionForm;
