import React from 'react';
import './App.css';
import Nav from './components/Nav';
import Home from './components/Home';
import About from './components/About';
import Request from './components/Request';
import Features from './components/Features';
import Contact from './components/Contact';


const App = () => {
  return (
    <>
      <Nav/>
      <Home/>
      <About/>
      <Request/>
      <Features/>
      <Contact/>
 

      <footer className="bg-[#501A89]  text-white py-6 text-center">
        <p>&copy; 2024 Sign Language Converter. All Rights Reserved.</p>
      </footer> 
    </>
  );
};

export default App;
