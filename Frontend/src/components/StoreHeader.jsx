import { useMemo } from "react";

export default function Header({
  cart,
  removeFromCart,
  decreaseQuantity,
  increaseQuantity,
  clearCart,
}) {
  // State Derivado
  const isEmpty = useMemo(() => cart.length === 0, [cart]);
  const cartTotal = useMemo(
    () => cart.reduce((total, item) => total + item.quantity * item.price, 0),
    [cart]
  );

  return (
    <header className="py-3">
      <div className="container-xl items-center">
        <div className=" flex justify-content-md-between items-center">
          <h1 className="text-white">Productos de Hardware Hacking</h1>
          <nav>
            <div className="carrito">
              <img
                className="img-fluid"
                src="https://cdn-icons-png.flaticon.com/512/181/181598.png"
                alt="imagen carrito"
              />

              <div id="carrito" className="bg-white p-3">
                {isEmpty ? (
                  <p className="text-center mt-3">No hay productos</p>
                ) : (
                  <>
                    <table className="table h-36 ">
                      <thead>
                        <tr>
                          <th>Imagen</th>
                          <th>Nombre</th>
                          <th>Precio</th>
                          <th>Cantidad</th>
                          <th></th>
                        </tr>
                      </thead>
                      <tbody>
                        {cart.map((product) => (
                          <tr key={product.id}>
                            <td>
                              <img
                                className="img-fluid"
                                src={product.image}
                                alt="imagen producto"
                              />
                            </td>
                            <td>{product.name}</td>
                            <td className="fw-bold">${product.price}</td>
                            <td>
                              <button
                                type="button"
                                className="btn btn-dark"
                                onClick={() => decreaseQuantity(product.id)}
                              >
                                -
                              </button>
                              {product.quantity}
                              <button
                                type="button"
                                className="btn btn-dark"
                                onClick={() => increaseQuantity(product.id)}
                              >
                                +
                              </button>
                            </td>
                            <td>
                              <button
                                className="btn btn-danger"
                                type="button"
                                onClick={() => removeFromCart(product.id)}
                              >
                                X
                              </button>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>

                    <p className="text-end">
                      Total pagar: <span className="fw-bold">${cartTotal}</span>
                    </p>
                    <button
                      className="btn btn-dark w-100 mt-3 p-2"
                      onClick={clearCart}
                    >
                      Vaciar Carrito
                    </button>
                  </>
                )}
              </div>
            </div>
          </nav>
        </div>
      </div>
    </header>
  );
}
