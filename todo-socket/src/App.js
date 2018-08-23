import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import socket from 'socket.io-client';
let io = socket();


io.on('hello', () => console.log('hello'));
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>
      </div>
    );
  }
}

export default App;
