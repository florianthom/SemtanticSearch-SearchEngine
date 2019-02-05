import React, {Component} from "react";
import {Container, Row, Col, Button} from "reactstrap";
// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getReadTime} from "../../actions/statisticsActions"
import PropTypes from "prop-types"
import axios from "axios";




class PageReadStatistics extends Component{


    componentDidMount(){
        this.props.getReadTime();
    }


    render(){
        var readtime = this.props.reducerOutputObject.readTime
        return (
            <div>
                <Container>
                {(readtime === undefined || readtime === null || Object.keys(readtime).length === 0) ? 0 : readtime.map(searched => (
                    <div key={searched[0]}>
                        <Container>
                            {searched[0]} {searched[1]}
                        </Container>
                    </div>))}
                    {console.log(readtime)}
                </Container>
            </div>
        );
    }


}



PageReadStatistics.propTypes = {
    getReadTime: PropTypes.func.isRequired,
    reducerOutputObject: PropTypes.object.isRequired,
}

const mapStateToProps = (state) => ({

    reducerOutputObject: state.statistics,
})

export default connect(mapStateToProps,
    {getReadTime} // redux mapDispatchToProps in short Object-notation-form
)(PageReadStatistics); // die Klasse