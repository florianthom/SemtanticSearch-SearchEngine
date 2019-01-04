// auch Container genannt
// Container werden Components genannt, die mit redux verbunden sind
// kurz: wenn redux state innerhalb eines Components benutzt wird, wird diese Component auch Container geannnt
// manchmal werden Components und Container separiert, wird hier nicht gemacht


// Verweis: https://reactstrap.github.io/components/modals/


import React, {Component} from "react";
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
import {connect} from "react-redux";
import {addPage} from "../../actions/pageActions";

class PageModal extends Component {
    state = {
        modal: false,
        title: ""
    }

    toggle = () => {
        this.setState({
            modal: !this.state.modal
        });
    }

    onChange = (event) => {
        this.setState({[event.target.name]: event.target.value});
    }

    onSubmit = (e) => {
        e.preventDefault(); // verhindert reload der kompletten page
        const newPage = {
            title: this.state.title,
            location: "test5",
            text:  "test5",
            number: ["456"]
        }

        // Add page via addPage action
        this.props.addPage(newPage);

        //close modal
        this.toggle();
    }

    render(){
        return(
            <div>
                <Button
                color="dark"
                style={{marginBottom: "2rem"}}
                onClick={this.toggle}>
                    Add Page
                </Button>

                <Modal
                isOpen={this.state.modal}
                toggle={this.toggle}>
                    <ModalHeader toggle={this.toggle}>
                        Add to Page List
                    </ModalHeader>
                    <ModalBody>
                        <Form onSubmit={this.onSubmit}>
                            <FormGroup>
                                <Label for="page"> Page </Label>
                                <Input
                                type="text"
                                name="title"
                                id="page"
                                placeholder="Add page"
                                onChange={this.onChange}>
                                
                                </Input>
                                <Button
                                color="dark"
                                style={{marginTop: "2rem"}}
                                block>
                                    Add Page
                                </Button>
                            </FormGroup>
                        </Form>
                    </ModalBody>
                </Modal>
            </div>
        );
    }
}

const mapStateToProps = (state) => ({
    page: state.page
});

export default connect(mapStateToProps, {addPage})(PageModal);