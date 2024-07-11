/* eslint-disable no-unused-vars */
// Nehimya
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter } from "react-router-dom"
import { UserProvider } from './context/userContext.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    {/* Zacarias */}
    <UserProvider>
      <App />
    </UserProvider>
  </BrowserRouter>
)