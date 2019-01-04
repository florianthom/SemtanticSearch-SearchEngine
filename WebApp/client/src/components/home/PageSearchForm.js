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

    onSubmit = (event) => {
        event.preventDefault(); // verhindert reload der kompletten page
        console.log(this.state)
        // Add page via addPage action
        this.props.getSearchResult(this.state);

    }

    onChange = (event) => {
        this.setState({[event.target.searchString]: event.target.value});
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
                                onChange={this.onChange}>
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

