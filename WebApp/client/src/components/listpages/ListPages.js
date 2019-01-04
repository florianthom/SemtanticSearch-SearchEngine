import React, {Component} from "react";
import {Container} from "reactstrap";
import PageModal from "./PageModal";
import PageList from "./PageList";

class ListPages extends Component{
    render(){
        return (
            <div>
                <Container>
                    <PageModal />
                    <PageList />
                </Container>
            </div>
        );
    }
}

export default ListPages;