import React, {Component} from "react";
import {Container, Row, Col, Button} from "reactstrap";
// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getMostOftenSearched} from "../../actions/statisticsActions"
import PropTypes from "prop-types"
import axios from "axios";




class ViewLonger4Seconds extends Component{

    render(){
        var readLonder4s = this.props.reducerOutputObject.results;
        return (
            <div>
                --------------------------------------------
                {console.log("readLonger")}
                {console.log(readLonder4s)}
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

export default connect(mapStateToProps,
    {getMostOftenSearched} // redux mapDispatchToProps in short Object-notation-form
)(ViewLonger4Seconds); // die Klasse