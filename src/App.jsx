import React from 'react';
import './index.css';
function App() {
  return (
    <div className="app-container">
    <div className="logo-container">
      <img src="/logo.svg" alt="Logo" />
    </div>
      <nav>
        <ul>
          <li>INICIO</li>
          <li>SERVICIOS</li>
          <li>HARDWARE HACKING</li>
          <li>NOSOTROS</li>
          <li>CONTACTOS</li>
          <li>LOGIN</li>
        </ul>
      </nav>
      <div className="ciberseguridad">
        CIBERSEGURIDAD
      </div>

      {/* Aquí puedes agregar más contenido o componentes */}

    </div>
  );
}

export default App;