import ChatMessage from "./ChatMessage";

function ChatHistory({ chatHistory }) {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        borderRadius: "8px",
        padding: "10px",
        height: "400px",
        overflowY: "auto",
        backgroundColor: "#f9f9f9",
      }}
    >
      {chatHistory.map((entry, index) => (
        <ChatMessage key={index} text={entry.text} type={entry.type} />
      ))}
    </div>
  );
}

export default ChatHistory;
