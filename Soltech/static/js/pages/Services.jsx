import React from 'react'
import ServiceCard from '../components/serviceCard'
import { servicesBD } from '../data/servicesBD'

const Services = () => {
  console.log(servicesBD)
  return (
    <>
        <div className='flex flex-col w-full h-auto bg-white items-center text-2xl py-6'>
            <h1>Nuestros servicios de ciberseguridad incluyen</h1>
           
            <div className='flex w-3/4 h-auto bg-white justify-center text-2xl py-6 flex-wrap'>
              {servicesBD.map((service) => (
                <ServiceCard
                  key = {service.id}
                  service ={service}
                />
            ))}
            </div>
        </div>
    </>
  )
}

export default Services