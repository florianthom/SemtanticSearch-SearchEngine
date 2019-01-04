//Verweis: https://reactstrap.github.io/components/navbar/

import React, { Component } from "react";
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink,
    UncontrolledDropdown,
    DropdownToggle,
    DropdownMenu,
    DropdownItem,
    Container
} from "reactstrap";

// since we dont bind custom functionalities like toggle via bind (instead we go with arrow-functions), we can ommit the constructor
class AppNavbar extends Component{
    state = {
        isOpen: false
    }

    toggle = () => {
        this.setState({
            isOpen: !this.state.isOpen
        });
    }

    render(){
        return (
            <div>
            <Navbar color="dark" dark expand="sm" className="mb-5">
                <Container>
                    <NavbarBrand href="/">Reports-Search-Engine</NavbarBrand>
                    <NavbarToggler onClick={this.toggle} />
                    <Collapse isOpen={this.state.isOpen} navbar>
                        <Nav className="ml-auto" navbar>
                            <NavItem>
                                <NavLink href="/">
                                    Home
                                </NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="/list">
                                    All Reports
                                </NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="https://github.com/FlorianTh2/SemtanticSearch-SearchEngine">
                                    Github
                                </NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="/about">
                                    About
                                </NavLink>
                            </NavItem>
                            <NavItem>
                                <NavLink href="/contact">
                                    Contact
                                </NavLink>
                            </NavItem>
                        </Nav>
                    </Collapse>
                </Container>
            </Navbar>
        </div>
        ); 
    }
}


export default AppNavbar