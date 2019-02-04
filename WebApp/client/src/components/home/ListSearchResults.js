import React, {Component} from "react";
import {Container, ListGroup, ListGroupItem, Button} from "reactstrap";
import {CSSTransition, TransitionGroup} from "react-transition-group";
import { Link } from 'react-router-dom'


// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getPages, deletePage} from "../../actions/pageActions"
import PropTypes from "prop-types"

class ListSearchResults extends Component{


    render(){
        if(!this.props.reducerOutputObject.searchResults){
            console.log("EMMPTYYY")
            return null;
        }
            const searchResultItem = this.props.reducerOutputObject.searchResults.map(result => (
                <ListGroupItem className="my-3" key={result._id.$oid}>
                {/*              why id.$oid? from python we have to send json to our backend
                             due to zeroRPC or RPC in generall all Attributes have to be serializable
                             normally _id not is 123412 ect but _id = ObjectId(123412) and that is not serializable
                             so json.utils made it serializable and so _id got converted to _id.$oid */}

                            <Link to={"/pages/" + result._id.$oid} style={{ textDecoration: 'none', color: "black"}}>
                            <div key={result._id.$oid}>
                                <h5>
                                    {result.title}
                                </h5>
                                <p>{result.date}</p>
                                {/* result.number is transmittet as string so this doesnt work well*/}                              
                                 <p>Fallnummer: {Array.isArray(result.number) ? result.number.map(number => (<span key={number}>{number} </span>)) : result.number}, Ort: {result.location}</p>
                                {/*<p>Fallnummer: {result.number}, Ort: {result.location}</p>*/}
                                    <p>{result.text.length < 150 ? result.text : result.text.substring(0,150) + "..."}</p>
                            </div>
                            </Link>
                            </ListGroupItem>
        ));

        return (
            <Container className="mt-5">
                <ListGroup>
                        {searchResultItem}
                </ListGroup>
            </Container>
        );
    }
}



const mapStateToProps = (state) => ({
    reducerOutputObject: state.search
});

export default connect(mapStateToProps,
null // redux mapDispatchToProps in short Object-notation-form
)(ListSearchResults); // die Klasse

