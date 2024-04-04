import React from "react";
import Cookies from "universal-cookie";
import LoginForm from "../components/LoginForm";

//instantiating Cookies class by creating cookies object
const cookies = new Cookies();

class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      email: "",
      password: "",
      error: "",
      isAuthenticated: false,
    };
  }

  componentDidMount = () => {
    this.getSession();
  }

// Get Session Method
  getSession = () => {
    //// Make a GET request to the "/api/session/" URL with "same-origin" credentials
    fetch("/api/session/", {
      credentials: "same-origin",
    })
    .then((res) => res.json()) //// Parse the response as JSON
    .then((data) => {
      console.log(data); // Log the response data to the console
      //// If the response indicates the user is authenticated
      if (data.isAuthenticated) {
        this.setState({isAuthenticated: true}); // Update the component's state
      } else {  // If the response indicates the user is not authenticated
        this.setState({isAuthenticated: false}); // Update the component's state
      }
    })
      //// Handle any errors that occurred during the fetch
    .catch((err) => {
      console.log(err);
    });
  }
  
//Who Am I method
  whoami = () => {
    fetch("/api/whoami/", {
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "same-origin",
    })
    .then((res) => res.json())
    .then((data) => {
      console.log("You are logged in as: " + data.email);
    })
    .catch((err) => {
      console.log(err);
    });
  }

  handlePasswordChange = (event) => {
    this.setState({password: event.target.value});
  }

  handleemailChange = (event) => {
    this.setState({email: event.target.value});
  }

  isResponseOk(response) {
    if (response.status >= 200 && response.status <= 299) {
      return response.json();
    } else {
      throw Error(response.statusText);
    }
  }

  //Login Mthod
  login = (event) => {
    event.preventDefault(); // Prevent the default form submission behavior
     // Make a POST request to the "/api/login/" URL with the form data
    fetch("/api/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": cookies.get("csrftoken"),
      },
      credentials: "same-origin",
      body: JSON.stringify({email: this.state.email, password: this.state.password}),
    })
    .then(this.isResponseOk)
    .then((data) => {
      console.log(data);
      this.setState({isAuthenticated: true, email: "", password: "", error: ""});
    })
    .catch((err) => {
      console.log(err);
      this.setState({error: "Email o contraseña incorrectas."});
    });
  }

  //Logout Method
  logout = () => {
    fetch("/api/logout", {
      credentials: "same-origin",
    })
    .then(this.isResponseOk)
    .then((data) => {
      console.log(data);
      this.setState({isAuthenticated: false});
    })
    .catch((err) => {
      console.log(err);
    });
  };


  // UI Rendering using bootstrap 
  render() {
    if (!this.state.isAuthenticated) {
      return (
        <LoginForm 
            email={this.state.email}
            password={this.state.password}
            error={this.state.error}
            handleemailChange={this.handleemailChange}
            handlePasswordChange={this.handlePasswordChange}
            login={this.login}
        />
      );
    }
    return (
      <div className="container mt-3">
        <p>Login exitoso</p>
      </div>
    )
  }
}

export default App;