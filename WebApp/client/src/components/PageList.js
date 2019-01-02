// Verweis zu: https://reactstrap.github.io/components/listgroup/

import React, {Component} from "react";
import {Container, ListGroup, ListGroupItem, Button} from "reactstrap";
import {CSSTransition, TransitionGroup} from "react-transition-group";

// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getPages, deletePage} from "../actions/pageActions"
import PropTypes from "prop-types"

var date = new Date();

class PageList extends Component{

    componentDidMount(){
        this.props.getPages();
    }

    onDeleteClick = (id) => {
        // calls the action deletePage
        this.props.deletePage(id)
    }

    render(){
        const {pages} = this.props.page;
        return (
            <Container>
                <ListGroup>
                    <TransitionGroup className="page-list">
                        {pages.map(({_id,date,title,text,number}) => (
                            <CSSTransition key={_id} timeout={500} classNames="fade">
                                <ListGroupItem>
                                    <Button
                                    className="remove-btn"
                                    color="danger"
                                    size="sm"
                                    onClick={this.onDeleteClick.bind(this,_id)}>

                                        &times;

                                    </Button>
                                    {title}
                                    <br />
                                    {_id}
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
    page: state.page
})

export default connect(mapStateToProps,
    {getPages,deletePage}
)(PageList);