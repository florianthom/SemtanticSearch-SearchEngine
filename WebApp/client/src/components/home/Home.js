import React, { Component } from 'react';
import PageSearchForm from "./PageSearchForm";
import ListSearchResults from "./ListSearchResults";
 
class Home extends Component {
  render() {
    return (
        <div>
          <PageSearchForm />
          <ListSearchResults />
        </div>
    );
  }
}
 
export default Home;