import React, {Component} from "react";
import {Container, ListGroup, ListGroupItem, Button} from "reactstrap";
import {CSSTransition, TransitionGroup} from "react-transition-group";
import uuid from "uuid";
import {connect} from "react-redux";
import {getPages} from "../actions/pageAction"
import PropTypes from "prop-types"

var date = new Date();

class PageList extends Component{

componentDidMount(){
    this.props.getPages();
}

    render(){
        const {pages} = this.props.page
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

PageList.PropTypes = {
    getPages: PropTypes.func.isRequired,
    page: PropTypes.object.isRequired
}

const mapStateToProps = (state) => ({
    page: state.page
})

export default connect(mapStateToProps, {getPages})(PageList);