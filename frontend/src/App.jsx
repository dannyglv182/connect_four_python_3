import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const numCols = 4;
  const [board, boardState] = useState([[4, 1], [4, 2], [4, 3], [4, 4],
         [3, 1], [3, 2], [3, 3], [3, 4],
         [2, 1], [2, 2], [2, 3], [2, 4],
         [1, 1], [1, 2], [1, 3], [1, 4]])

  async function makeMove(row, column) {
    const res = await fetch ("http://localhost:8000/move", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({row: row, column: column})
    });
    const data = await res.json();
    console.log(data.board);
    boardState(data.board);
}
  

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        {/*
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <button onClick={() => makeMove(1,1)}>
          call the backend.
        </button>
        */}
        <div>
          <h1>game board</h1>
          {board.map(([row, col], index) => (
          <span>
          <button
          key={index}
          onClick={() => makeMove(row, col)}
          >
          {row},{col}
          </button>

          {(index + 1) % 4 === 0 && <br />}
          </span>
          
          ))}
        </div>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>

    </>
  )
}

export default App
