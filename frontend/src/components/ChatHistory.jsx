import ChatMessage from "./ChatMessage";

function ChatHistory({ chatHistory }) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",  // Center the chat window horizontally
        width: "100%",  // Ensure the container takes up the full width of the screen
      }}
    >
      <div
        style={{
          width: "1200px",  // Set the width of the chat window to 1200px
          padding: "10px",
          border: "1px solid #ccc",
          borderRadius: "8px",
          height: "1000px",
          overflowY: "auto",
          backgroundColor: "#f9f9f9",
        }}
      >
        {chatHistory.map((entry, index) => (
          <ChatMessage 
            key={index} 
            text={entry.text} 
            type={entry.type} 
            toolsUsed={entry.toolsUsed}  // Pass toolsUsed to the ChatMessage component
          />
        ))}
      </div>
    </div>
  );
}

export default ChatHistory;
