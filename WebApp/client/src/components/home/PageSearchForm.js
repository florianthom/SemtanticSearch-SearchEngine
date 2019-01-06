
import React from "react";
import PropTypes from "prop-types"
import {connect} from "react-redux";
import {getSearchResult} from "../../actions/searchActions"
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    Form,
    FormGroup,
    Label,
    Input
} from "reactstrap";
import { DateRangePicker, SingleDatePicker, DayPickerRangeController } from 'react-dates';

import '../../App.css';

import 'react-dates/initialize';
import 'react-dates/lib/css/_datepicker.css';






class PageSearchForm extends React.Component{


    constructor(){
        super();
        this.state = {
        searchString: "",
        startDate: null,
        endDate: null,
        focusedInput: null};
    }

    // funktionen wie onSubmit oder onChange müssen eigentlich im Constructor gebindet werden
    // da wir aber = (event) => {} haben,also eine arrow-method, machen wir das damit
    onSubmit = (event) => {
        // muss erste Anweisung sein
        // verhindert reload der kompletten page
        event.preventDefault();
        // falls man versucht console.log("hello" + this.state) zu machen return er immer hello + object

        // Add page via addPage action

        if(this.state.startDate && this.state.endDate && this.state.startDate.toDate() < this.state.endDate.toDate())
        {
            this.props.getSearchResult(this.state.searchString);
            // hier muss noch das Date mit rein
        }
        else{
            this.props.getSearchResult(this.state.searchString);

        }
        
    }

    onChange = (event) => {
        this.setState({
            // [event.target.name] ist praktisch der name des <input> tags
            // event.target.value ist sein Wert
            // beides ist nur generisch, konkret heißt das z.B.
            // searchString: "hallo123"
            [event.target.name]: event.target.value
            
        });
        if(this.state.startDate){
            console.log(this.state.startDate.toDate())
        }
    }

    render(){
        return (
            <div className="container searchform">
                <div className="my-5">
                    <h1>Sucheingabe</h1>
                </div>
                <Form onSubmit={this.onSubmit}>
                            <FormGroup>
                                <Input
                                className="mb-3"
                                type="text"
                                name="searchString"
                                placeholder="Search String"
                                onChange={this.onChange.bind(this)}
                                >                                
                                </Input>

                                
                                <DateRangePicker
                                    startDateId="startDate"
                                    endDateId="endDate"
                                    startDate={this.state.startDate} // momentPropTypes.momentObj or null,
                                    endDate={this.state.endDate} // momentPropTypes.momentObj or null,
                                    onDatesChange={({ startDate, endDate }) => this.setState({ startDate, endDate })} // PropTypes.func.isRequired,
                                    focusedInput={this.state.focusedInput} // PropTypes.oneOf([START_DATE, END_DATE]) or null,
                                    onFocusChange={focusedInput => this.setState({ focusedInput })} // PropTypes.func.isRequired,
                                /> 
                                

                                <div className="container pl-5 pr-5">
                                <Button
                                color="dark"
                                style={{marginTop: "2rem"}}
                                block>
                                    Search
                                </Button>
                                </div>
                            </FormGroup>
                        </Form>
            </div>
        );
    }
}

PageSearchForm.propTypes = {
    getSearchResult: PropTypes.func.isRequired,
    search: PropTypes.object.isRequired
}


const mapStateToProps = (state) => ({
    search: state.search
})

export default connect(mapStateToProps,
    {getSearchResult} // redux mapDispatchToProps in short Object-notation-form
)(PageSearchForm);

