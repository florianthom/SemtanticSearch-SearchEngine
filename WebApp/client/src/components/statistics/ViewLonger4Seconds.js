import React, {Component} from "react";
import {Container, Row, Col, Button} from "reactstrap";
// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import PropTypes from "prop-types"




class ViewLonger4Seconds extends Component{

    render(){
            var readLonger4s = this.props.reducerOutputObject.results.result_articles_ids_with_counter;
            return (
                <div className="mt-5">
                    <Row className="mt-5">
                        <Col xs={12} className="text-center">
                        <h1 className="mt-5">
                            Die meist gelesenen* Artikel
                        </h1>
                        </Col>
                    </Row>

                    {!readLonger4s ? (
                        <div>
                            <Row>
                                <Col xs={12} className="text-center">
                                    <h5>
                                        Bisher wurde keine Seite länger als 4s gelesen
                                    </h5>
                                </Col>
                            </Row>
                        </div>
                    ) : (
                        readLonger4s.map(item => (
                            <div key={item[0]}>
                                <Row className="mt-5 text-center">
                                    <Col xs={6}>
                                        <h5>{item[0]}</h5>
                                    </Col>
                                    <Col xs={6}>
                                        <h5>{item[1]}</h5>
                                    </Col>
                                </Row>
                            </div>

                        ))
                    )}
                    <div className="mt-5 pt-5 float-right pb-5">
                                *gelesen: Als gelesen wird ein Artikel angenommen, sobald dieser länger als 4 Sekunden betrachtet wurde
                    </div>
                </div>
                
        );
    }
}




ViewLonger4Seconds.propTypes = {
    reducerOutputObject: PropTypes.object.isRequired,
}

const mapStateToProps = (state) => ({

    reducerOutputObject: state.statistics,
})

export default connect(mapStateToProps,)(ViewLonger4Seconds); // die Klasse