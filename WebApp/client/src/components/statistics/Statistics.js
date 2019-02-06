import React, {Component} from "react";
import {Container, Row, Col, Button} from "reactstrap";
import MostOftenSearchedStatistics from "./MostOftenSearchedStatistics";
import ViewLonger4Seconds from "./ViewLonger4Seconds";
import {connect} from "react-redux";
import PropTypes from "prop-types"
import { PAGES_LOADING } from "../../actions/types";
import {getMostOftenSearched} from "../../actions/statisticsActions"


class Statistics extends Component{


    componentDidMount(){
        this.props.getMostOftenSearched();
    }


    render(){
        // checked ob die Asynchrone Operation in componentDidMount abgeschlossen ist (der return vorliegt)
        // Why? Page gets render twice: 1. when user clicks 2. when asynchronous methods in componentDidMount finished
        // if no conditional rendering here: for the first rendering = variables == undefined that is Error and Failures
        //  with the read of the variables
        const state = this.props.reducerOutputObject.results 

        return (
            state ? (
                <Container>
                    <MostOftenSearchedStatistics />
                    <ViewLonger4Seconds />
                </Container>
                ) : 
                (
                    <div> 
                        <Row className="text-center">
                            <Col xs={12}>
                                <h1>Loading...</h1>
                            </Col>
                        </Row>
                    </div>
                )
         );
    }
}


Statistics.propTypes = {
    getMostOftenSearched: PropTypes.func.isRequired,
    reducerOutputObject: PropTypes.object.isRequired,
}

const mapStateToProps = (state) => ({
    reducerOutputObject: state.statistics,
})
export default connect(mapStateToProps,
    {getMostOftenSearched} 
)(Statistics); 