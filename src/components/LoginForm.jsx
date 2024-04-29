import { useState } from 'react';

export default function LoginForm({ email, password, handleemailChange, handlePasswordChange, login }) {
    const [showText, setShowText] = useState(false);

    const handleButtonClick = () => {
        setShowText(true);
        // Perform any other actions you need here
    };

    return (
        <>
            <main className="bg-gray-200/25 text-gray-900">
                <div className="flex items-center h-full w-full py-14">
                    <div className="w-full bg-white rounded shadow-lg p-8 m-4 md:max-w-sm md:mx-auto">
                        <img className="w-full object-cover mb-6" src="logoblack.svg" alt="Service" />
                        <h2 className="w-full text-xl uppercase font-bold">Iniciar sesión</h2>
                        <form className="mb-4 mt-5 flex flex-col" action="/" method="post" onSubmit={login}>
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
                                    onChange={handleemailChange}
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
                                onClick={handleButtonClick}
                            >
                                Acceder
                            </button>
                        </form>
                        {/* {showText && <p className='flex justify-center text-green-600'>Usuario identificado</p>} */}
                        {showText}
                        <a className="text-blue-700 text-center text-sm" href="/login">
                            ¿Olvidaste tu contraseña?
                        </a>
                    </div>
                </div>
            </main>
        </>
    );
}
