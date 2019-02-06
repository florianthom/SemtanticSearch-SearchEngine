import React, {Component} from "react";
import {Container, Row, Col, Button} from "reactstrap";
// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getMostOftenSearched} from "../../actions/statisticsActions"
import PropTypes from "prop-types"
import axios from "axios";


class MostOftenSearchedStatistics extends Component{

    render(){
        var mostOftenSearched = this.props.reducerOutputObject.results.most_often_search_words;
        return (
            <div>
                <Container>
                <Row className="mb-5">
                    <Col xs={12}>
                        <h1 className="text-center">
                            Die meist gesuchten Begriffe
                        </h1>
                    </Col>
                </Row>
                <Row className="mb-5">
                    <Col xs={6} className="text-center">
                        <h3>
                            Suchbegriff
                        </h3>
                    </Col>
                    <Col xs={6} className="text-center">
                        <h3>
                            Aufgerufen
                        </h3>
                    </Col>
                </Row>
                {
                    mostOftenSearched.map(searched => (
                    <Row key={searched[0]}>
                        <Col xs={6} className="text-center">
                            <h5>{searched[0]}</h5>
                        </Col>
                        <Col xs={6} className="text-center">
                            <h5>{searched[1]}x</h5>
                        </Col>
                    </Row>
                    ))
                }
                </Container>
                </div>
        
        );
    }
}


MostOftenSearchedStatistics.propTypes = {
    reducerOutputObject: PropTypes.object.isRequired,
}

const mapStateToProps = (state) => ({
    reducerOutputObject: state.statistics,
})

export default connect(mapStateToProps)(MostOftenSearchedStatistics);