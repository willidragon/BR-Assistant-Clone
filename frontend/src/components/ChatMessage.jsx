function ChatMessage({ text, type }) {
    return (
      <div
        style={{
          marginBottom: "10px",
          textAlign: type === "question" ? "right" : "left",
        }}
      >
        <div
          style={{
            display: "inline-block",
            padding: "10px",
            borderRadius: "8px",
            backgroundColor: type === "question" ? "#0084ff" : "#e4e6eb",
            color: type === "question" ? "#fff" : "#000",
          }}
        >
          {text}
        </div>
      </div>
    );
  }
  
  export default ChatMessage;
  