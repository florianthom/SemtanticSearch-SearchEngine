
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
    Input,
    Container,
    Row,
    Col
} from "reactstrap";
import { DateRangePicker, SingleDatePicker, DayPickerRangeController } from 'react-dates';

import '../../App.css';

import 'react-dates/initialize';
import 'react-dates/lib/css/_datepicker.css';






class PageSearchForm extends React.Component{


    constructor(){
        super();
        this.state = {
        
        // seachStringTotal={searchString, date}
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
            console.log("start Date end date")
        }
        
        if(this.state.searchString)
        {
            var payload = {
                searchString: this.state.searchString ? this.state.searchString : null,
                dateFROM: this.state.startDate ? this.state.startDate.toDate().toString() : null,
                dateTO: this.state.endDate ? this.state.endDate.toDate().toString() : null
            }
            console.log(payload)
            this.props.getSearchResult(payload);

        }

    }

    onChange = (event) => {
        console.log("name of event: ")
        console.log(event.target.name)
        this.setState({
            // [event.target.name] ist praktisch der name des <input> tags
            // event.target.value ist sein Wert
            // beides ist nur generisch, konkret heißt das z.B.
            // searchString: "hallo123"
            [event.target.name]: event.target.value
            
        });
        console.log("state:")
        console.log(this.setState)
        if(this.state.startDate){
            console.log(this.state.startDate.toDate())
        }
    }


    // this.setState({searchString: suggestionForThisWordOutOfSearchterm[0]}) &&

    setterForState = (newSearchString) => {
        console.log("set search value");
        this.state.searchString = newSearchString;
        return true
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
                                id="searchtermInputField"
                                >                                
                                </Input>


                                {console.log(this.props.reducerOutputObject.searchResults.synonyme)}
                                {/* wenn noch keine Suchergebnisse vorliegen oder der Suchstring nicht vorliegt, mach nicht, ansonsten outputte*/}
                                {/* {!(this.props.reducerOutputObject.searchResults == undefined || this.props.reducerOutputObject.searchString == undefined) ? this.props.reducerOutputObject.searchString in this.props.reducerOutputObject.searchResults.synonyme ? (
                                    <div className="text-left mb-2">
                                    <span className="mr-3">Meinten Sie:</span> 
                                        {this.props.reducerOutputObject.searchResults.synonyme[this.props.reducerOutputObject.searchString].map(synonym => (
                                            <span key={synonym[0]} className="mr-2">{synonym[0]}</span>
                                        ))}
                                        </div>
                                ):
                                (
                                    <div>
                                        {/* keine Synonyme vorhanden für den gesamten Suchterm }
                                    </div>
                                ) : <div>{/* es gibt keine Synonyme momentan }</div>} */}

                                {!(this.props.reducerOutputObject.searchResults === undefined || this.props.reducerOutputObject.searchString === undefined || Object.keys(this.props.reducerOutputObject.searchResults.synonyme).length === 0) ? (
                                    <div className="text-left">
                                        <Row className="mr-3"><Col xs={12}> Meinten Sie:</Col></Row>

                                        {Object.keys(this.props.reducerOutputObject.searchResults.synonyme).map(attribute => (
                                            <div key={attribute}>
                                                <Container>
                                                    <Row className="text-left"> 
                                                        <Col xs={3} className="mr-3">Für {attribute}:</Col>
                                                        <Col xs={8}>
                                                            {this.props.reducerOutputObject.searchResults.synonyme[attribute].map(suggestionForThisWordOutOfSearchterm => (
                                                            <span key={suggestionForThisWordOutOfSearchterm[0]} className="mr-2">{<Button color="link" onClick={(event) => {this.setterForState(suggestionForThisWordOutOfSearchterm[0]) && (document.getElementById("searchtermInputField").value = suggestionForThisWordOutOfSearchterm[0]) && this.onSubmit(event)} /* hier muss Suchterm geändert werden und Submitted werden */}>{suggestionForThisWordOutOfSearchterm[0]}</Button>}</span>
                                                    ))}
                                                    </Col>
                                                    </Row>

                                                </Container>
                                            </div>
                                             

                                        ))}




{/* (document.getElementById("searchtermInputField").value = suggestionForThisWordOutOfSearchterm[0])  */}









                                    </div>
                                ) : <div>{/* es gibt keine Synonyme momentan */}</div>}




                                
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
    reducerOutputObject: PropTypes.object.isRequired
}


const mapStateToProps = (state) => ({
    reducerOutputObject: state.search
})

export default connect(mapStateToProps,
    {getSearchResult} // redux mapDispatchToProps in short Object-notation-form
)(PageSearchForm);

