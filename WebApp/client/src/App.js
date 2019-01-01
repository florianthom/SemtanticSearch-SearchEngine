import React, { Component } from 'react';
import AppNavbar from "./components/AppNavbar"
import PageList from "./components/PageList"

import "bootstrap/dist/css/bootstrap.min.css";
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">


        <AppNavbar />
        <PageList />



      </div>
    );
  }
}

export default App;
