import React, { useState } from 'react';

export default function RegisterForm({ handleRegister, error }) {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [subscribe, setSubscribe] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();
    handleRegister(firstName, lastName, email, password, subscribe);
  };

  return (
    <>
      <main className="bg-gray-200/25 text-gray-900">
        <div className="flex items-center h-full w-full py-14">
          <div className="w-full bg-white rounded shadow-lg p-8 m-4 md:max-w-sm md:mx-auto">
            <h2 className="w-full text-xl uppercase font-bold">Registro</h2>
            <form className="mb-4 mt-5 flex flex-col" onSubmit={handleSubmit}>
              <div className="mb-4">
                <label htmlFor="firstName" className="block text-s mb-1">Nombre</label>
                <input
                  className="w-full border rounded p-2 outline-none focus:shadow-outline"
                  type="text"
                  name="firstName"
                  id="firstName"
                  placeholder="Nombre"
                  value={firstName}
                  onChange={(e) => setFirstName(e.target.value)}
                  required
                />
              </div>
              <div className="mb-4">
                <label htmlFor="lastName" className="block text-s mb-1">Apellido</label>
                <input
                  className="w-full border rounded p-2 outline-none focus:shadow-outline"
                  type="text"
                  name="lastName"
                  id="lastName"
                  placeholder="Apellido"
                  value={lastName}
                  onChange={(e) => setLastName(e.target.value)}
                  required
                />
              </div>
              <div className="mb-4">
                <label htmlFor="email" className="block text-s mb-1">Correo electrónico</label>
                <input
                  className="w-full border rounded p-2 outline-none focus:shadow-outline"
                  type="email"
                  name="email"
                  id="email"
                  placeholder="Correo electrónico"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              <div className="mb-6">
                <label htmlFor="password" className="block text-s mb-1">Contraseña</label>
                <input
                  className="w-full border rounded p-2 outline-none focus:shadow-outline"
                  type="password"
                  name="password"
                  id="password"
                  placeholder="Contraseña"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              <div className="mb-4">
                <label htmlFor="subscribe" className="block text-s mb-1">
                  ¿Suscribirse a nuestro boletín?
                </label>
                <input
                  type="checkbox"
                  name="subscribe"
                  id="subscribe"
                  checked={subscribe}
                  onChange={(e) => setSubscribe(e.target.checked)}
                />
              </div>
              {error && <p className="text-red-500 text-xs italic">{error}</p>}
              <button className="bg-blue-500 hover:bg-blue-700 text-white uppercase text-sm font-semibold px-6 py-2 rounded">
                Registrarse
              </button>
            </form>
            <a className="text-blue-700 text-center text-sm" href="/login">
              Volver al inicio de sesión
            </a>
          </div>
        </div>
      </main>
    </>
  );
}
