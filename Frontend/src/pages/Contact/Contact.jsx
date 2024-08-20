export default function Contact() {
  const teamMembers = [
    {
      name: "Andres Rojas",
      github: "https://github.com/arojaspe",
    },
    {
      name: "David Martinez",
      github: "https://github.com/DavidMT7",
    },
    {
      name: "Edwin Chaves",
      github: "https://github.com/eachaves",
    },
  ];

  return (
    <div className="p-4 w-full px-40 bg-gray-100 rounded-md shadow-md text-justify">
      <img className="mx-auto w-96" src="logoblack.svg" alt="Logo" />
      <h1 className="text-2xl font-bold text-center mt-4">Equipo de trabajo</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
        {teamMembers.map((member, index) => (
          <div
            key={index}
            className="bg-white rounded-lg shadow-lg p-6 flex flex-col items-center"
          >
            <h2 className="text-xl font-semibold mb-2">{member.name}</h2>
            <a
              href={member.github}
              target="_blank"
              className="text-blue-500 hover:text-blue-900"
            >
              {member.github}
            </a>
          </div>
        ))}
      </div>
      <div className="text-center mt-8">
        <p className="text-lg">Universidad Nacional de Colombia, 2024</p>
      </div>
    </div>
  );
}
