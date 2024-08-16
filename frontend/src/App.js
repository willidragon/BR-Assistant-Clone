import logo from "./logo.svg";
import "./App.css";
import QuestionForm from "./components/QuestionForm";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>Chat With MPCS</p>
        <QuestionForm />
      </header>
    </div>
  );
}

export default App;
