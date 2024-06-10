export default function ItemCard({ product, addToCart }) {
  const { name, image, descriptionShort, price } = product;
  return (
    <main>
      <div className="w-80 mx-5 mt-16 bg-white shadow-xl rounded-lg text-gray-900">
        <div className="rounded-t-lg h-auto overflow-hidden flex flex-col items-center text-justify text-wrap">
          <img className="w-full object-cover" src={image} alt="Service" />
          <p className="text-center px-5 pt-3">{name}</p>
          <p className="text-base px-3 py-4">{descriptionShort}</p>
          <p className="text-xl font-semibold px-3 pb-4 text-red-400">
            USD${price}
          </p>
          <button
            type="button"
            className="btn text-base btn-dark bg-slate-600/50 p-2 rounded-lg mb-3 w-100"
            onClick={() => addToCart(product)}
          >
            Agregar al Carrito
          </button>
        </div>
      </div>
    </main>
  );
}
