// src/routes.jsx
import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import Layout from './components/Layout'; // Asegúrate de que este componente exista
import Home from './pages/Home/Home';
import Services from './pages/Services/Services';
import Store from './pages/Products/Store'; // Asegúrate de que este componente exista
import AboutUs from './pages/AboutUs/About';
import Contact from './pages/Contact/Contact';
import Login from './pages/Login/Login';
import Register from './pages/Register/Register';
import Checkout from './pages/Checkout/Checkout';
import ErrorPage from './pages/ErrorPage'; // Página de error

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    errorElement: <ErrorPage />, // Página de error
    children: [
      { path: "/", element: <Home /> },
      { path: "/services", element: <Services /> },
      { path: "/store", element: <Store /> },
      { path: "/about-us", element: <AboutUs /> },
      { path: "/contact", element: <Contact /> },
      { path: "/login", element: <Login /> },
      { path: "/register", element: <Register /> },
      { path: "/checkout", element: <Checkout /> },
    ],
  },
]);

export default router;
