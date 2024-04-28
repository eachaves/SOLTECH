import React from "react";
import Cookies from "universal-cookie";
import RegisterForm from "../components/RegisterForm";

// Instantiating Cookies class by creating cookies object
const cookies = new Cookies();

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      email: "",
      password: "",
      error: "",
      isAuthenticated: false,
    };
  }

  componentDidMount() {
    this.getSession();
  }

  // Get Session Method
  getSession = () => {
    // Aquí iría la lógica para obtener la sesión actual, si existe
  }

  // Who Am I method
  whoami = () => {
    // Aquí iría la lógica para verificar quién está autenticado
  }

  handleUsernameChange = (event) => {
    this.setState({username: event.target.value});
  }

  handleEmailChange = (event) => {
    this.setState({email: event.target.value});
  }

  handlePasswordChange = (event) => {
    this.setState({password: event.target.value});
  }

  isResponseOk = (response) => {
    // Aquí iría la lógica para verificar si la respuesta de la API está bien
  }

  // Register Method
  register = (event) => {
    event.preventDefault();
    // Aquí iría la lógica para manejar el registro
    // Por ejemplo, hacer una solicitud POST a tu API de registro
  }

  // Logout Method
  logout = () => {
    // Aquí iría la lógica para cerrar la sesión
  }

  // UI Rendering
  render() {
    if (!this.state.isAuthenticated) {
      return (
        <RegisterForm 
          username={this.state.username}
          email={this.state.email}
          password={this.state.password}
          error={this.state.error}
          handleUsernameChange={this.handleUsernameChange}
          handleEmailChange={this.handleEmailChange}
          handlePasswordChange={this.handlePasswordChange}
          register={this.register}
        />
      );
    }
    return (
      <div className="container mt-3">
        <p>Registro exitoso</p>
        <button onClick={this.logout}>Cerrar sesión</button>
      </div>
    )
  }
}

export default App;