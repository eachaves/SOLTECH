"use client";

import { useEffect, useRef, useState } from "react";

export function useModal() {
    const stateRef = useRef({});
    const onLoad = (state) => (stateRef.current = state);

    return { stateRef, onLoad };
}

export function useInnerModal(
    open,
    onOpen,
    onClose,
    onLoad,
) {
    const modalState = useState(open ? true : null);
    const [isOpen, setNullishModal] = modalState;

    useEffect(() => {
        onLoad({ isOpen, setModal: (v) => setNullishModal(v) });
    }, [onLoad, isOpen, setNullishModal]);

    useEffect(() => {
        if (isOpen == null) return;

        if (isOpen) {
            document.body.classList.add("overflow-hidden");
            onOpen();
            return;
        }

        document.body.classList.remove("overflow-hidden");
        onClose();
    }, [isOpen, onOpen, onClose]);

    return { isOpen, setNullishModal };
}

export const ModalState = {
    isOpen: null,
    setModal: () => {},
};
