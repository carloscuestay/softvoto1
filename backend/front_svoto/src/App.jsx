import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'


import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href=" " target="_blank">
          <img src="https://previews.123rf.com/images/dirkercken/dirkercken1403/dirkercken140301620/26969365-entrar-icono-o-usuario-o-acceso-por-miembros-bot%C3%B3n-bandera-del-web-site.jpg" className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_Bk_oSvd-ClsqVuuTSYK9m3xFQmo4vtZplw&usqp=CAU" className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>DJANGO Y REACT COMBINACION MORTAL</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          Visitante numero {count}
        </button>
        <p>
        <img src="https://i.pinimg.com/736x/13/74/22/137422088fd0cba64a95bae8b3c8f6ff.jpg" className="logo" />
          Bienvenido a nuestro Ecosistema Digital D3CSec
        </p>
      </div>
      <p className="read-the-docs">
        Ingresa de forma segura con nuestro cifrado militar
      </p>
    </>
  )
}

export default App
