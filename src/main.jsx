import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import NavBar from './components/NavBar.jsx'
import Services from './pages/Services.jsx'
import { Outlet, RouterProvider, createBrowserRouter } from "react-router-dom"

const Layout = () => {
  return (
    <div>
      <NavBar />
      <Outlet />

    </div>
  )
}

const router = createBrowserRouter([{
  path: '/',
  element: <Layout />,
  children: [
    {
    path: '/',
    element: <App />
  },
  {
    path: '/servicios',
    element: <Services />
  },
  {
    path: '/nosotros',
    element: <App />
  },
  {
    path: '/login',
    element: <App />
  }]
}])

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router} />
)
