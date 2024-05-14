import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

// HERE IS THE MAGIC
function App() {
  
  const [currentTime, setCurrentTime] = useState(0)
  const [theJoke, setTheJoke] = useState(0) 

  useEffect(() => {
    fetch("http://thewizard.online:5000/time")
        .then(res => res.json()).then(data => 
	      { setCurrentTime(data.time);
    });
  }, []);
  useEffect(() => {
    fetch("http://thewizard.online:5000/joke")
	.then(res => res.json()).then(data =>
	      { setTheJoke(data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
	<p>The current time is {currentTime} - time for a random joke.</p>
	<p>{theJoke.setup} {theJoke.punchline}</p>  
      </header>
    </div>
  );
}

export default App;
