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


class PageSearchForm extends React.Component{


    constructor(){
        super();
        this.state = {"searchString": ""}
    }

    // funktionen wie onSubmit oder onChange müssen eigentlich im Constructor gebindet werden
    // da wir aber = (event) => {} haben,also eine arrow-method, machen wir das damit
    onSubmit = (event) => {
        // muss erste Anweisung sein
        // verhindert reload der kompletten page
        event.preventDefault();
        // falls man versucht console.log("hello" + this.state) zu machen return er immer hello + object




            console.log(this.state.searchString)
            // Add page via addPage action
            this.props.getSearchResult(this.state.searchString);
        
    }

    onChange = (event) => {
        this.setState({
            // [event.target.name] ist praktisch der name des <input> tags
            // event.target.value ist sein Wert
            // beides ist nur generisch, konkret heißt das z.B.
            // searchString: "hallo123"
            [event.target.name]: event.target.value  
            
        });
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
                                type="text"
                                name="searchString"
                                placeholder="Search String"
                                onChange={this.onChange.bind(this)}
                                >                                
                                </Input>

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

