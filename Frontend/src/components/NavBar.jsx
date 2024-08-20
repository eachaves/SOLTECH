// src/components/NavBar.jsx
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Cookies from "universal-cookie";

const cookies = new Cookies();

export default function NavBar() {
  const menuItems = [
    { title: "INICIO", link: "/" }, // Coincide con "/"
    { title: "SERVICIOS", link: "/services" }, // Coincide con "/services"
    { title: "HARDWARE HACKING", link: "/SHtore" }, // Coincide con "/store"
    { title: "NOSOTROS", link: "/about-us" }, // Coincide con "/about-us"
    { title: "CONTÁCTANOS", link: "/contact" } // Coincide con "/contact"
  ];

  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const verifyToken = () => {
      const token = cookies.get("token");
      setIsAuthenticated(!!token);
    };

    verifyToken();
  }, []);

  return (
    <>
      <header className="flex w-full">
        <div className="w-1/4">
          <img
            className="w-90 px-7 py-4"
            src="/logo.svg"
            alt="Logo"
            style={{ fill: "white" }}
          />
        </div>
        <nav className="w-3/4 flex items-center justify-center px-3">
          <ul className="flex px-15 justify-between w-3/4 items-center">
            {menuItems.map(({ title, link }) => (
              <Link key={link} to={link}>
                <p className="hover:underline hover:text-blue-800 transition ease-in-out duration-200 font-normal text-white tracking-wider mt-3">
                  {title}
                </p>
              </Link>
            ))}
            <li>
              {isAuthenticated ? (
                <button
                  className="rounded-full border-white border-2 transition-all px-5 py-1 font-normal tracking-wider text-white hover:bg-blue-800/35"
                  onClick={() => {
                    cookies.remove("token");
                    setIsAuthenticated(false);
                  }}
                >
                  LOGOUT
                </button>
              ) : (
                <Link to="/login">
                  <button className="rounded-full border-white border-2 transition-all px-5 py-1 font-normal tracking-wider text-white hover:bg-blue-800/35">
                    LOGIN
                  </button>
                </Link>
              )}
            </li>
          </ul>
        </nav>
      </header>
    </>
  );
}
