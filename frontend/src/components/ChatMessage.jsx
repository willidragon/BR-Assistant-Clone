function ChatMessage({ text, type, toolsUsed }) {
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
          fontSize: "18px", // Set the font size to 18px
          position: "relative",
        }}
      >
        {text}
        {toolsUsed && (
          <div
            style={{
              marginTop: "10px",
              paddingTop: "10px",
              fontSize: "14px",
              color: toolsUsed === "No tools used" ? "gray" : "green",
              borderTop: "1px solid #ccc",
              textAlign: "left",
            }}
          >
            {toolsUsed === "No tools used" ? "No tools used" : `Tools used: ${toolsUsed}`}
          </div>
        )}
      </div>
    </div>
  );
}

export default ChatMessage;
