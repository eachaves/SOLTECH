export default function ServiceCard ({service}) {

    const {id, name, image, description} = service;

    return (
        <>
            <main>
            <div className="w-64 mx-4 mt-16 bg-white shadow-xl rounded-lg text-gray-900">
                <div className="rounded-t-lg h-auto overflow-hidden flex flex-col items-center text-justify text-wrap">
                    
                    <img className="w-full object-cover" src={`/${image}.png`} alt="Service" />
                    <p className="text-center px-5 pt-3">{name}</p>
                    <p className="text-sm px-3 py-4">{description}</p>
                </div>
            </div>

            </main>
            
        </>

    );



}