import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import NavBar from "./components/NavBar.jsx";
import Services from "./pages/Services.jsx";
import Temp from "./pages/Temp.jsx";
import Login from "./pages/Login.jsx";
import Store from "./pages/Store.jsx";
import About from "./pages/About.jsx";
import { Outlet, RouterProvider, createBrowserRouter } from "react-router-dom";

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
        element: <Temp />,
      },
      {
        path: "/login",
        element: <Login />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);
