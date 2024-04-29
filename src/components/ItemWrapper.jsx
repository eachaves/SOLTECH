

import { Modal, useModal } from "./Modal";
import ItemCard from "./ItemCard";
import { ProductModal } from "./ProductModal";

export default function ItemWrapper({product}) {
  const { onLoad, stateRef } = useModal();

  return (
    <>
      <ItemCard
        key={product.id}
        item={product}
        onClick={() => stateRef.current.setModal(true)}
      />
      <Modal
        onLoad={onLoad}
        className="relative h-3/5 w-[23.5rem] rounded-xl bg-pattern-19-to-b from-portGore to-portGore bg-cover  p-0"
      >
        <ProductModal key={product.id} item={product} />
      </Modal>
    </>
  );
}
