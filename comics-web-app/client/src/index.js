// filepath: /comics-web-app/comics-web-app/client/src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './assets/styles.css'; // Assuming you have a global stylesheet

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);