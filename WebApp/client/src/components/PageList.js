import React, {Component} from "react";
import {Container, ListGroup, ListGroupItem, Button} from "reactstrap";
import {CSSTransition, TransitionGroup} from "react-transition-group";
import uuid from "uuid";
var date = new Date();


class PageList extends Component{
    state = {
        pages: [
            {id: uuid(), date: (date.getDay()-1).toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),title: "test1",location: "test123",text: "text123",number: ["1234",""]},

            {id: uuid(), date: (date.getDay()-1).toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),title: "test2",location: "test123",text: "text123",number: ["1234",""]},

            {id: uuid(), date: (date.getDay()-1).toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),title: "test3",location: "test123",text: "text123",number: ["1234",""]}
        ]
    }

    render(){
        const {pages} = this.state;
        return (
            <Container>
                <Button 
                    color="dark"
                    style={{marginBottom: "2rem"}}
                    onClick={() => {
                        const title = prompt("Enter page");
                        if(title){
                            this.setState(state => ({
                                pages: [...state.pages, {id: uuid(), date: (date.getDay()-1).toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),title: title, text: "addedText1", number: ["1111",""]}]
                            }));
                        }}
                        }>
                    Add Page
                </Button>
                <ListGroup>
                    <TransitionGroup className="page-list">
                        {pages.map(({id,date,title,text,number}) => (
                            <CSSTransition key={id} timeout={500} classNames="fade">
                                <ListGroupItem>
                                    <Button
                                        className="remove-btn"
                                        color="danger"
                                        size="sm"
                                        onClick={()=> {
                                            this.setState(state => ({
                                                pages: state.pages.filter(page => page.id !== id)
                                            }));
                                        }}>
                                        &times;
                                        </Button>
                                        {title}
                                </ListGroupItem>
                            </CSSTransition>
                        ))}
                    </TransitionGroup>
                </ListGroup>
            </Container>
        );
    }
}

export default PageList;