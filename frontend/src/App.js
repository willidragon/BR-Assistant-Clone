import logo from "./logo.svg";
import "./App.css";
import QuestionForm from "./components/QuestionForm";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Welcome to chatbot</p>
        <QuestionForm />
      </header>
    </div>
  );
}

export default App;
