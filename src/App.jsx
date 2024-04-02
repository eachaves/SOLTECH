import React from 'react';
import NavBar from './components/NavBar';


function App() {

  return (
    <main className= "w-full">

      <NavBar /> 

      <section className='px-12 w-4/4 relative grid h-[33.5rem] grid-rows-2 '>
        <h1 className="ciberseguridad row-start-1 text-white">
          01 <br/>
          CIBERSEGURIDAD
        </h1>
        <p className='row-start-2 self-center text-3xl text-white/75'>Mejora tu ciberseguridad, inteligencia y caza de amenazas</p>
        <div className='row-start-3 justify-self-center w-60'>

          <p className='font-semibold text-white tracking-wider text-3xl pb-2'>
            Creando un líder en ciberseguridad  
          </p>      
          <p className='font-extralight text-white tracking-wider w-64'>
            Líderes en protección a más de 100 empresas nacionales e internacionales.
          </p>
        </div>
      </section>

    </main>

  );
}

export default App;