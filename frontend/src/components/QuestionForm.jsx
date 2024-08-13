import { useState } from "react";
import axios from "axios";

const api = axios.create({
  baseURL: "https://expert-acorn-wvr6p5q4vgrhq9g-8000.app.github.dev",
});

function QuestionForm() {
  const [question, setQuestion] = useState(""); // Correct way to destructure useState
  const [answer, setAnswer] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await api.post("/chat", { message: question });
    setAnswer(response.data.answer);
  };

  return (
    <form>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />
      <button type="submit" onClick={handleSubmit}>
        Submit
      </button>
    </form>
  );
}

export default QuestionForm;
