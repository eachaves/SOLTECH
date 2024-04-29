import { productsBD } from "../data/productsBD";

import ItemCard from "../components/ItemCard";
import StoreHeader from "../components/StoreHeader";
import { useState, useEffect, useMemo } from "react";

export default function Store() {
  const initialCart = () => {
    const localStorageCart = localStorage.getItem("cart");
    return localStorageCart ? JSON.parse(localStorageCart) : [];
  };

  const [data] = useState(productsBD);
  const [cart, setCart] = useState(initialCart);

  const MIN_ITEMS = 1;
  const MAX_ITEMS = 5;

  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(cart));
  }, [cart]);

  function addToCart(item) {
    const itemExists = cart.findIndex((product) => product.id === item.id);
    if (itemExists >= 0) {
      // existe en el carrito
      if (cart[itemExists].quantity >= MAX_ITEMS) return;
      const updatedCart = [...cart];
      updatedCart[itemExists].quantity++;
      setCart(updatedCart);
    } else {
      item.quantity = 1;
      setCart([...cart, item]);
    }
  }

  function removeFromCart(id) {
    setCart((prevCart) => prevCart.filter((product) => product.id !== id));
  }

  function decreaseQuantity(id) {
    const updatedCart = cart.map((item) => {
      if (item.id === id && item.quantity > MIN_ITEMS) {
        return {
          ...item,
          quantity: item.quantity - 1,
        };
      }
      return item;
    });
    setCart(updatedCart);
  }

  function increaseQuantity(id) {
    const updatedCart = cart.map((item) => {
      if (item.id === id && item.quantity < MAX_ITEMS) {
        return {
          ...item,
          quantity: item.quantity + 1,
        };
      }
      return item;
    });
    setCart(updatedCart);
  }

  function clearCart() {
    setCart([]);
  }
  const isEmpty = useMemo(() => cart.length === 0, [cart]);

  return (
    <>
      <StoreHeader
        cart={cart}
        removeFromCart={removeFromCart}
        decreaseQuantity={decreaseQuantity}
        increaseQuantity={increaseQuantity}
        clearCart={clearCart}
        isEmpty={isEmpty}
      />

      <main>
        <div className="flex flex-wrap w-full h-full bg-white mb-6 items-center justify-center text-2xl">
          {data.map((product) => (
            <ItemCard
              key={product.id}
              product={product}
              setCart={setCart}
              addToCart={addToCart}
            />
          ))}
        </div>
      </main>
    </>
  );
}
