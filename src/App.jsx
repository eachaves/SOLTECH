import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  return (
    <>
      <div id="root">
        {/* Añade tus enlaces aquí, aplicando la clase 'nav-link' a cada uno */}
        <a href="#inicio" className="nav-link">Inicio</a>
        <a href="#servicios" className="nav-link">Servicios</a>
        <a href="#hardware-hacking" className="nav-link">Hardware Hacking</a>
        <a href="#nosotros" className="nav-link">Nosotros</a>
        <a href="#contactos" className="nav-link">Contactos</a>
        <a href="#login" className="nav-link">Login</a>
      </div>
      {/* El resto de tu contenido */}
    </>
  );
}

export default App;