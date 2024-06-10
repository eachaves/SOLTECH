import { useState } from "react";
import axios from "axios";

export default function RegisterForm() {
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleRegister = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/auth/signup/",
        {
          username: username,
          first_name: firstName,
          last_name: lastName,
          email: email,
          password: password,
          is_superuser: false,
        }
      );
      if (response.status === 200 || response.status === 201) {
        setMessage("Registro exitoso. Ahora puedes iniciar sesión.");
      }
    } catch (error) {
      setMessage("Error en el registro. Inténtalo de nuevo.");
    }
  };

  return (
    <>
      <main className="bg-gray-200/25 text-gray-900">
        <div className="flex items-center h-full w-full py-14">
          <div className="w-full bg-white rounded shadow-lg p-8 m-4 md:max-w-sm md:mx-auto">
            <img
              className="w-full object-cover mb-6"
              src="logoblack.svg"
              alt="Service"
            />
            <h2 className="w-full text-xl uppercase font-bold">Registro</h2>
            <form className="mb-4 mt-3 flex flex-col" onSubmit={handleRegister}>
              <div className="mb-4">
                <label htmlFor="username" className="block text-s mb-1">
                  Nombre de usuario
                </label>
                <input
                  className="w-full border rounded p-2 outline-none focus:shadow-outline"
                  type="text"
                  name="username"
                  id="username"
                  placeholder="Nombre de usuario"
                  value={username}
                  onChange={handleUsernameChange}
                />
              </div>
              <div className="mb-4">
                <label htmlFor="firstName" className="block text-s mb-1">
                  Nombre
                </label>
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
                <label htmlFor="lastName" className="block text-s mb-1">
                  Apellido
                </label>
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
                <label htmlFor="email" className="block text-s mb-1">
                  Correo electrónico
                </label>
                <input
                  className="w-full border rounded p-2 outline-none focus:shadow-outline"
                  type="email"
                  name="email"
                  id="email"
                  placeholder="Correo electrónico"
                  value={email}
                  onChange={handleEmailChange}
                />
              </div>
              <div className="mb-6">
                <label htmlFor="password" className="block text-s mb-1">
                  Contraseña
                </label>
                <input
                  className="w-full border rounded p-2 outline-none focus:shadow-outline"
                  type="password"
                  name="password"
                  id="password"
                  placeholder="Contraseña"
                  value={password}
                  onChange={handlePasswordChange}
                />
              </div>
              <button
                className="bg-blue-500 hover:bg-blue-700 text-white uppercase text-sm font-semibold px-6 py-2 rounded"
                type="submit"
              >
                Registrarse
              </button>
            </form>
            {message && <p className="text-center mt-4">{message}</p>}
            <a className="text-blue-700 text-center text-sm" href="/login">
              ¿Ya tienes cuenta? Inicia sesión aquí
            </a>
          </div>
        </div>
      </main>
    </>
  );
}
