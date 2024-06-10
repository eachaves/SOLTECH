import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Cookies from "universal-cookie";

export default function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();
  const cookies = new Cookies();

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/auth/login/",
        {
          email: email,
          password: password,
        }
      );
      const token = response.data.access;
      console.log(token);
      if (response.status === 200) {
        setMessage("Datos correctos");
        cookies.set("token", token);
        navigate("/admin");
        window.location.reload(); // Add this line to reload the page
      }
    } catch (error) {
      setMessage("Datos incorrectos. Inténtalo de nuevo.");
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
            <h2 className="w-full text-xl uppercase font-bold">
              Iniciar sesión
            </h2>
            <form className="mb-4 mt-5 flex flex-col" onSubmit={handleLogin}>
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
                Acceder
              </button>
            </form>
            {message && <p className="text-center mt-4">{message}</p>}
            <a className="text-blue-700 text-center text-sm" href="/register">
              Regístrate aquí
            </a>
          </div>
        </div>
      </main>
    </>
  );
}
