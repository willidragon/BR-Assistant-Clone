import { useState } from "react";

function InputForm({ onSubmit }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (question.trim() === "") return;
    onSubmit(question);
    setQuestion("");
  };

  return (
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
  );
}

export default InputForm;
