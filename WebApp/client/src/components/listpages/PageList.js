// Verweis zu: https://reactstrap.github.io/components/listgroup/

import React, {Component} from "react";
import {Container, ListGroup, ListGroupItem, Button} from "reactstrap";
import {CSSTransition, TransitionGroup} from "react-transition-group";

// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getPages, deletePage} from "../../actions/pageActions"
import PropTypes from "prop-types"

var date = new Date();

class PageList extends Component{

    // ist eine react-lifecycle-method
    // lifecycle-methods runs in react at specific points
    // The componentDidMount() method runs after the component 
    // output has been rendered to the DOM. This is a good place to set up a timer
    componentDidMount(){
        // gettet den state.page auf this.props.page
        this.props.getPages(); // kommt von mapDispatchToProps
    }

    onDeleteClick = (id) => {
        // calls the action deletePage
        this.props.deletePage(id) // redux kommt von mapDispatchToProps
    }

    render(){
            // state.page represents the whole initial state
             // state.page.pages represents the pages array inside the state.page
        const {pages} = this.props.page; // kommt von mapStateToProps
        return (
            <Container>
                <ListGroup>
                    <TransitionGroup className="page-list">
                        {pages.map(({_id,date,title,text,number}) => (
                            <CSSTransition key={_id} timeout={10} classNames="fade">
                                <ListGroupItem className="my-2">
                                    <Button
                                    className="remove-btn"
                                    color="danger"
                                    size="sm"
                                    onClick={this.onDeleteClick.bind(this,_id)}>

                                        &times;

                                    </Button>
                                    {title} <span className="float-right">{date}</span>
                                    
                                </ListGroupItem>
                            </CSSTransition>
                        ))}
                    </TransitionGroup>
                </ListGroup>
            </Container>
        );
    }
}

PageList.propTypes = {
    getPages: PropTypes.func.isRequired,
    page: PropTypes.object.isRequired
}

const mapStateToProps = (state) => ({
    // Sinn = redux-store.state.page wird gemapped auf das hier lokale this.props.page
    // page, da wir unter unserem rootReducer aka reducers/index.js in combineReducers unseren
    // PageReducer unter dem Property page gespeichert haben
    // daher wird hier auch state.pages unter this.props.page verfügbar gemacht

    // state.page represents the whole initial state
    // state.page.pages represents the pages array inside the state.page

    // und von diesem reducer wollen wir nur das page-prop von dem Return (=state)

    // das page bei stae.page muss mit dem reducer matchen
    page: state.page
})

export default connect(mapStateToProps,
    {getPages,deletePage} // redux mapDispatchToProps in short Object-notation-form
)(PageList); // die Klasse

