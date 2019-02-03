import React, {Component} from "react";
import {Container} from "reactstrap";
// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getPage} from "../../actions/pageActions"
import PropTypes from "prop-types"


class Pages extends Component{

    componentDidMount(){
        this.props.getPage(this.props.match.params.id);
    }

    render(){
        const page = this.props.reducerOutputObject.page; // kommt von mapStateToProps
        return (
            <div>
                
                    {page.title}
            </div>
        );
    }
}

Pages.propTypes = {
    getPage: PropTypes.func.isRequired,
    reducerOutputObject: PropTypes.object.isRequired
}

const mapStateToProps = (state) => ({
    // Sinn = redux-store.state.page wird gemapped auf das hier lokale this.props.page
    // page, da wir unter unserem rootReducer aka reducers/index.js in combineReducers unseren
    // PageReducer unter dem Property page gespeichert haben
    // daher wird hier auch state.pages unter this.props.page verfügbar gemacht

    // state.page represents the whole initial state
    // state.page.pages represents the pages array inside the state.page

    // und von diesem reducer wollen wir nur das page-prop von dem Return (=state)

    // das page bei state.page muss mit dem reducer matchen !!!!!!!!
    reducerOutputObject: state.pages 
    // name because you can access all values with the names/values you see in pageReducer
    // reducerOutputObject: state.reducername
})

export default connect(mapStateToProps,
    {getPage} // redux mapDispatchToProps in short Object-notation-form
)(Pages); // die Klasse