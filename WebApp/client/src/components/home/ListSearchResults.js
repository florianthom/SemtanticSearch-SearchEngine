import React, {Component} from "react";
import {Container, ListGroup, ListGroupItem, Button} from "reactstrap";
import {CSSTransition, TransitionGroup} from "react-transition-group";

// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getPages, deletePage} from "../../actions/pageActions"
import PropTypes from "prop-types"

class ListSearchResults extends Component{


    render(){
        console.log("bei render");        
        const searchResultItem = this.props.search.map(result => (
            <div>
                <h3>
                    {
                        result.title
                    }
                </h3>
            </div>
        ));
/* 
        <div>
        <h3>
            
            {results.title}
        </h3>
    </div> */


        return (
            <Container>
                <ListGroup>
                    <ListGroupItem>
                        {searchResultItem}
                    </ListGroupItem>
                </ListGroup>
            </Container>
        );
    }
}

{/* 
                    <TransitionGroup className="page-list">
                        {pages.map(({_id,date,title,text,number}) => (
                            <CSSTransition key={_id} timeout={10} classNames="fade">
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
*/}




const mapStateToProps = (state) => ({
    search: state.search.searchResults
});

export default connect(mapStateToProps,
null // redux mapDispatchToProps in short Object-notation-form
)(ListSearchResults); // die Klasse

