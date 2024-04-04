import React from 'react'
import { useState } from 'react'

export default function Login({ email, password, error, handleemailChange, handlePasswordChange, login}) {
    console.log(email, password, error, handleemailChange, handlePasswordChange, login)
  return (
    <>
        <body class="bg-gray-200/25 text-gray-900">
            <div class="flex items-center h-full w-full py-14">
                <div class="w-full bg-white rounded shadow-lg p-8 m-4 md:max-w-sm md:mx-auto">
                <img className="w-full object-cover mb-6" src='logoblack.svg' alt="Service" />
                    <h2 class="w-full text-xl uppercase font-bold">Iniciar sesión</h2>      
                    <form class="mb-4 mt-5 flex flex-col" action="/" method="post" onSubmit={login}>
                        <div class="mb-4">
                            <label for="email" class="block text-s mb-1">Correo electrónico</label>
                            <input class="w-full border rounded p-2 outline-none focus:shadow-outline" type="email" name="email" id="email" placeholder="Correo electrónico" value={email} onChange={handleemailChange}/>
                        </div>
                        <div class="mb-6">
                            <label for="password" class="block text-s mb-1">Contraseña</label>
                            <input class="w-full border rounded p-2 outline-none focus:shadow-outline" type="password" name="password" id="password" placeholder="Contraseña" value={password} onChange={handlePasswordChange} />
                        </div>
                        <button class="bg-blue-500 hover:bg-blue-700 text-white uppercase text-sm font-semibold px-6 py-2 rounded">Acceder</button>
                    </form>
                    <a class="text-blue-700 text-center text-sm" href="/login">¿Olvidaste tu contraseña?</a>
                </div>
            </div>
        </body>
    </>
  )
}
