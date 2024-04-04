import { Link } from "react-router-dom";

export default function NavBar() {
    const menuItems =  [
        { title: "INICIO", link: "/" },
        { title: "SERVICIOS", link: "/servicios" },
        { title: "HARDWARE HACKING", link: "/tienda" },
        { title: "NOSOTROS", link: "/nosotros" },
        { title: "CONTÁCTANOS", link: "/contacto" },
    ];
    const login = [
        { title: "LOGIN", link: "/login" }
    ]

    return (
        <>
            <header className="flex w-full h-auto">
                <div className="w-1/4 ">
                    <img className="w-90 flex flex-row px-7 py-4" src="/logo.svg" alt="Logo" style={{ fill: "white" }} />
                </div>
                <nav className="w-3/4 flex flex-row items-center justify-center px-3 py-3">
                    <ul className="flex px-15 justify-between w-3/4">
                        {menuItems.map(({ title, link }) => (
                            <Link key={link} to={link}>
                                <p className="hover:underline hover:text-blue-800 transition ease-in-out duration-200 font-normal text-white tracking-wider">
                                    {title}
                                </p>
                            </Link>
                        ))}
                        <li>
                            {login.map(({ title, link }) => (
                                <Link key={link} to={link}>
                                    <p className="rounded-full border-white border-2 transition-all px-5 py-1 font-normal tracking-wider text-white hover:bg-blue-800/35">
                                        {title}
                                    </p>
                                </Link>
                            ))}
                            
                        </li>
                    </ul>
                </nav>
            </header>
        </>
    );
}
