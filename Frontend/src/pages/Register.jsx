import { useState, useEffect } from "react";
import Cookies from "universal-cookie";
import RegisterForm from "../components/RegisterForm";

const cookies = new Cookies();

export default function Register() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    getSession();
  }, []);

  const getSession = () => {
    // Aquí iría la lógica para obtener la sesión actual, si existe
  };

  const whoami = () => {
    // Aquí iría la lógica para verificar quién está autenticado
  };

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const isResponseOk = (response) => {
    // Aquí iría la lógica para verificar si la respuesta de la API está bien
  };

  const register = (event) => {
    event.preventDefault();
    // Aquí iría la lógica para manejar el registro
    // Por ejemplo, hacer una solicitud POST a tu API de registro
  };

  const logout = () => {
    // Aquí iría la lógica para cerrar la sesión
  };

  return (
    <>
      {!isAuthenticated ? (
        <RegisterForm
          username={username}
          email={email}
          password={password}
          error={error}
          handleUsernameChange={handleUsernameChange}
          handleEmailChange={handleEmailChange}
          handlePasswordChange={handlePasswordChange}
          register={register}
        />
      ) : (
        <div className="container mt-3">
          <p>Registro exitoso</p>
          <button onClick={logout}>Cerrar sesión</button>
        </div>
      )}
    </>
  );
}
