import React, { Component } from 'react';
import AppNavbar from "./components/AppNavbar";
import Error from "./components/Error";
import {Provider} from 'react-redux';
import store from "./store";
import "bootstrap/dist/css/bootstrap.min.css";
import './App.css';
import About from "./components/about/About";
import Contact from "./components/contact/Contact";
import Home from "./components/home/Home";
import ListPages from "./components/listpages/ListPages";
import Pages from "./components/Pages/Pages"
import {BrowserRouter, Route, Switch} from "react-router-dom";
import 'react-dates/initialize';



class App extends Component {
  render() {
    return (
      <Provider store={store}>
        {/*
          kann immer nur 1 child haben deshalb muss Switch vor den Routes kommen
          bzw. wenn wir ein Element haben, welches sich über alle Pages erstreckt z.B.
          Navbar, brauchen wir trotzdem noch 1 dev um alles (Switch brauchen wir trotzdem
          für Error-Component)
        */}
        <BrowserRouter> 
          <div className="">

              {/* 
                kann replaced werden mit <div> </div> dann jedoch wird die 
                Error-Componente auf jeder Route angezeigt
                */}
              <AppNavbar />
              <Switch> 
                {/* 
                  exact sagt, dass der Pfad / exakt / sein muss
                  andernfalls matched / auch bei /about /contact usw.
                */}
                <Route path="/" component={Home} exact />
                <Route path="/pages" component={ListPages} exact/> 
                <Route path="/pages/:id" component={Pages} exact />
                <Route path="/about" component={About} />
                <Route path="/contact" component={Contact} />
                <Route component={Error} />
              </Switch>
            </div>

        </BrowserRouter>
      </Provider>
    );
  }
}

export default App;
