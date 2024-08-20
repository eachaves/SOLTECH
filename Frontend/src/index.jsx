import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/index.css'; // Asegúrate de que los estilos estén correctamente aplicados
import { RouterProvider, createBrowserRouter, Outlet } from 'react-router-dom'; // Importa Outlet aquí
import NavBar from './components/NavBar';
import Home from './pages/Home/Home';
import Services from './pages/Services/Services';
import Hardware from './pages/Products/Store';
import AboutUs from './pages/AboutUs/About';
import Contact from './pages/Contact/Contact';
import Login from './pages/Login/Login';
import Register from './pages/Register/Register';
import Checkout from './pages/Checkout/Checkout';

const Layout = () => {
  return (
    <div>
      <NavBar />
      <Outlet /> {/* Asegúrate de usar Outlet aquí */}
    </div>
  );
};

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/services",
        element: <Services />,
      },
      {
        path: "/hardware",
        element: <Hardware />,
      },
      {
        path: "/about-us",
        element: <AboutUs />,
      },
      {
        path: "/contact",
        element: <Contact />,
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/register",
        element: <Register />,
      },
      {
        path: "/checkout",
        element: <Checkout />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router} />
);
