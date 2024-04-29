import { useRef } from "react";
import { createPortal } from "react-dom";
import { useInnerModal } from "./useModal";

export default function Modal({
    children,
    open = false,
    onLoad,
    onOpen = () => undefined,
    onClose = () => undefined,
    ...props
}) {
    const { isOpen, setNullishModal } = useInnerModal(
        open,
        onOpen,
        onClose,
        onLoad
    );

    if (!isOpen) return null;

    return createPortal(
        <Content setState={setNullishModal} {...props}>
            {children}
        </Content>,
        document.body
    );
}

function Content({
    children,
    className,
    bgClassName,
    useContainer = true,
}) {
    const modalRef = useRef(null);

    

    return (
        <dialog
            className={`fixed inset-0 z-50 flex h-full w-full items-center justify-center bg-black/30 text-black ${bgClassName}`}
            onClick={(e) => e.stopPropagation()}
        >
            {useContainer ? (
                <section
                    className={`h-72 w-[32rem] rounded-xl bg-gray-50 p-8 ${className}`}
                    ref={modalRef}
                >
                    {children}
                </section>
            ) : (
                children
            )}
        </dialog>
    );
}

// TODO: Make Header and Footer of Modal
