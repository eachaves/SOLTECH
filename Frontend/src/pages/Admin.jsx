import { useEffect, useState } from "react";
import axios from "axios";
import Cookies from "universal-cookie";

const cookies = new Cookies();

export default function Admin() {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const token = cookies.get("token");
    if (!token) {
      setError("No hay token de autenticación. Inicie sesión primero.");
      return;
    }

    const fetchUsers = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/auth/users/",
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        setUsers(response.data);
      } catch (error) {
        setError("Error al cargar la lista de usuarios.");
      }
    };

    fetchUsers();
  }, []);

  return (
    <div className="container bg-white/80 p-6 rounded-xl mx-auto mt-8">
      <h1 className="text-2xl font-bold mb-4">Panel de Administrador</h1>
      {error && <p className="text-red-500">{error}</p>}

      <div className="grid grid-cols-3 gap-4 mt-4">
        {users.map((user) => (
          <div
            key={user.id}
            className="border border-gray-200 rounded p-4 shadow-md"
          >
            <h2 className="text-lg font-semibold mb-2">{user.username}</h2>
            <p>Email: {user.email}</p>
            <p>Nombre: {user.first_name}</p>
            <p>Apellido: {user.last_name}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
