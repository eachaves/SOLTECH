import { useState } from "react";




export function ProductModal({product}) {
  const [modalStage, setModalStage] = useState(1);

  return (
    <section className="h-full rounded-xl text-black">
      {modalStage === 1 && (
        <>
          <p className="flex h-12 items-center justify-end rounded-t-xl bg-plum px-2 py-1 text-right text-xl font-semibold">
            ELO
            <div className="group relative cursor-help">
              <div className="invisible absolute -top-[3.5rem] left-1/2 z-20 flex w-72 -translate-x-1/2 -translate-y-1/2 transform flex-col items-center justify-center gap-1 whitespace-pre-line rounded-lg bg-white p-3 leading-4 text-black shadow-md shadow-gray-800 transition-all group-hover:visible group-hover:animate-fade-in">
                <p className="text-center font-sans text-base font-normal leading-4">
                  El ELO es el puntaje de valoración obtendio de las
                  calificaciones de los usuarios asesorados. Entre más alto,
                  mejor.
                </p>
                
              </div>
            </div>
          </p>
          {/* <Image
            src={item.photoUrl}
            loader={({ src }) => `${src}?random=${item.id}`}
            alt=""
            className="-mt-6 mb-3 ml-8 w-36 rounded-full"
            width={100}
            height={100}
          /> */}
          <div className="mt-3 flex h-14 flex-col justify-center bg-plum leading-tight">
            <p className=" line-clamp-2 w-4/5 items-center px-6 text-lg font-semibold leading-tight">
             
            </p>
          </div>
          <div className="mt-3 flex h-52 flex-col justify-between">
            <p className=" mb-3 line-clamp-[7] w-full items-center px-6 text-base font-light leading-tight">
            </p>
            <button
              className="mx-auto my-auto mb-3 flex w-48 items-center justify-center rounded-xl bg-plum py-2 font-sans hover:bg-plum-light-20"
              onClick={() => setModalStage(2)}
            >
              <p>Especialidades</p>
            </button>
          </div>
        </>
      )}
    </section>
  );
}
