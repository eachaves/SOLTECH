import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import NavBar from "./components/NavBar.jsx";
import Services from "./pages/Services.jsx";
import Login from "./pages/Login.jsx";
import Store from "./pages/Store.jsx";
import About from "./pages/About.jsx";
import Admin from "./pages/Admin.jsx";
import Register from "./pages/Register.jsx";
import { Outlet, RouterProvider, createBrowserRouter } from "react-router-dom";
import Contact from "./pages/Contact.jsx";

export const Layout = () => {
  return (
    <div>
      <NavBar />
      <Outlet />
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
        element: <App />,
      },
      {
        path: "/servicios",
        element: <Services />,
      },
      {
        path: "/tienda",
        element: <Store />,
      },
      {
        path: "/nosotros",
        element: <About />,
      },
      {
        path: "/contacto",
        element: <Contact />,
      },
      {
        path: "/login",
        element: <Login />,
      },
      {
        path: "/admin",
        element: <Admin />,
      },
      {
        path: "/register",
        element: <Register />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
