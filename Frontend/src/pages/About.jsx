export default function About() {
  return (
    <>
      <div className="p-4 w-full px-40 bg-gray-100 rounded-md shadow-md text-justify">
        <img className="mx-auto w-96" src="logoblack.svg"></img>
        <h2 className="text-xl font-bold mb-4">Visión:</h2>
        <p className="mb-6">
          Para el 2027, aspiramos a ser una compañía líder en Colombia en la
          implementación y prestación de servicios profesionales de
          ciberseguridad. Seremos reconocidos por nuestros clientes gracias a
          nuestra transparencia y compromiso con la seguridad de sus datos y
          sistemas. Nuestra actuación siempre estará guiada por la integridad y
          la honestidad, y nos mantendremos ágiles y proactivos frente a las
          amenazas informáticas, asegurando la innovación y la vanguardia en
          nuestros procesos.
        </p>

        <h2 className="text-xl font-bold mb-4">Misión:</h2>
        <p className="mb-6">
          Ofrecemos la prestación de servicios profesionales, implementación,
          soluciones y productos de ciberseguridad, seguridad ofensiva y
          seguridad de la información para el sector corporativo, público y
          privado. Soportados para ello en alianzas estratégicas con proveedores
          confiables de ciberseguridad e infraestructura de alto nivel.
        </p>

        <h2 className="text-xl font-bold mb-4">Propuesta de valor</h2>
        <p className="mb-6">
          Nos dedicamos a proveer consultorías en servicios de ciberseguridad
          para red team, blue team y cacería de amenazas, complementadas con la
          venta de herramientas en seguridad ofensiva. Nos comprometemos con el
          desarrollo profesional de software ofreciendo soluciones
          personalizadas. Integramos prácticas sostenibles que respetan el medio
          ambiente, fomentamos una cultura corporativa de respeto y
          colaboración, y valoramos el crecimiento personal y profesional de
          nuestro equipo.
        </p>

        <h2 className="text-xl font-bold mb-4">Quiénes somos:</h2>
        <p className="mb-6">
          Somos una empresa dedicada a la consultoría especializada en
          ciberseguridad. Ofrecemos soluciones integrales desde evaluaciones
          personalizadas Blue Team y Red Team (de ataque y defensa), servicio de
          integración de tecnologías completas y de vanguardia, y venta de
          productos de hardware y software de ciberseguridad.
        </p>

        <h2 className="text-xl font-bold mb-4">Segmento de mercado:</h2>
        <p>
          Empresas de diferentes tamaños y sectores que buscan evaluar y
          fortalecer su seguridad cibernética sobre todo industrias bancarias
          gubernamentales y militares. Organizaciones en busca de servicios de
          auditoría o medición de seguridad cibernética y/o atención a
          incidentes. Personas interesadas en herramientas de seguridad
          ofensiva.
        </p>
        <h2 className="text-xl font-bold mb-4">Modelo de negocio:</h2>
        <p className="mb-6">
          Consulta especializada en ciberseguridad:
          <br />
          Realizamos evaluaciones exhaustivas de los sistemas de información de
          empresas u organizaciones, identificando posibles vulnerabilidades y
          riesgos de seguridad.
          <br />
          Ofrecemos asesoramiento personalizado para mitigar los riesgos
          identificados y mejorar la seguridad de los sistemas.
        </p>

        <p className="mb-6">
          Venta de hardware y software especializado en ciberseguridad:
          <br />
          Operamos una tienda online donde ofrecemos hardware diseñado para
          identificar y prevenir ataques cibernéticos, así como licencias de
          antivirus y antimalware.
          <br />
          Proporcionamos soluciones de software para fortalecer la seguridad de
          los sistemas informáticos.
        </p>

        <h2 className="text-xl font-bold mb-4">Reglas del negocio:</h2>
        <p className="mb-6">
          Medios de promoción y captación de clientes:
          <br />
          Utilizamos una variedad de medios digitales, como anuncios en redes
          sociales, Google Adwords, SEO y telemercadeo, para dar a conocer
          nuestros servicios y captar la atención de nuestra audiencia objetivo.
        </p>

        <div className="mb-6">
          <h2 className="text-xl font-bold mb-4">
            Canales de comunicación disponibles:
          </h2>
          <ul className="list-disc list-inside">
            <li>
              Ofrecemos múltiples canales de comunicación, incluyendo WhatsApp,
              llamadas telefónicas, mensajería por email y chat interno en redes
              sociales, para brindar asistencia y resolver dudas generales, así
              como para atraer nuevos clientes.
            </li>
          </ul>
        </div>

        <div className="mb-6">
          <h2 className="text-xl font-bold mb-4">
            Líneas de soluciones ofrecidas:
          </h2>
          <ul className="list-disc list-inside">
            <li>Consultoría y evaluación de ciberseguridad:</li>
            <li>
              Los clientes pueden conocer nuestros servicios a través de nuestro
              sitio web y contactarnos para solicitar consultoría y evaluación
              de ciberseguridad.
            </li>
            <li>
              Procedemos a visitar al cliente, analizamos sus sistemas de
              información y ofrecemos una cotización de soluciones.
            </li>
            <li>
              El pago se puede realizar mediante transferencia bancaria o a
              través de nuestra pasarela de pagos.
            </li>
          </ul>
        </div>

        <div>
          <h2 className="text-xl font-bold mb-4">Tienda online:</h2>
          <ul className="list-disc list-inside">
            <li>
              Nuestro sitio web incluye una tienda online con un catálogo de
              productos organizado y categorizado.
            </li>
            <li>
              Los clientes pueden seleccionar los productos deseados, realizar
              una orden de compra y elegir el servicio de mensajería deseado.
            </li>
            <li>
              Los pagos se procesan de manera segura a través de nuestra
              pasarela de pagos integrada.
            </li>
          </ul>
        </div>
      </div>
    </>
  );
}
