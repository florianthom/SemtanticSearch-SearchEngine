import React, {Component} from "react";
import {Container, Row, Col, Button} from "reactstrap";
// muss importiert werden, da wir redux verwenden
import {connect} from "react-redux";
import {getPage} from "../../actions/pageActions"
import PropTypes from "prop-types"
import axios from "axios";




class Pages extends Component{

    constructor(props)
    {
        super(props);

        // Binden von Eventhandlern
        // binds the function onUnload to the component instance from Pages
        // warum? Generel-problem: sonst hat Funktion keinen Zugriff auf die Klassenattribute
        // warum? Diffrence in 'this'
        //  in non-strict mode ist das default binding von this das globale Objekt,
        //  in strict mode: context (von this) lost after passing the handler as callback
        //  in JS: classes are executed in strict mode

        // wenn man in render binden möchte (nicht im ctor)
        // mit arrow functions (z.B. onChange={e => this.handleChange(e)}) kann man bind 
        //  (z.B. onChange={this.handleChange.bind(this)}) ) ersetzen
        this.onUnload = this.onUnload.bind(this);
        
        
        this.startTime = null;
    }



    onUnload(event)
    {
        console.log("hellooww")
        var time = Math.abs(Date.now() - this.startTime); // in ms
        if(time > 4000)
        {
            axios.post(`/api/statistics/${this.props.reducerOutputObject.page._id}`);
        }
        axios.post(`/api/pages/${this.props.reducerOutputObject.page._id}`, {time});

        // event.returnValue = "Hellooww" //-> if not commented: user will get a prompt
    }

    // lifecircle method
    // called if user enter pages and all Elements without js are loaded
    componentDidMount(){
        this.props.getPage(this.props.match.params.id);

        // callback function = passing function to another function
        // first arg: type of the event like "click"
        // second arg: the function we want to call when the event occurs (aka a callback)
        window.addEventListener("beforeunload", this.onUnload);
        this.startTime = Date.now();

    }

    // lifecircle method
    // called if user leaves page
    componentWillUnmount()
    {
        // why? otherwise the listener is on every following page also
        window.removeEventListener("beforeunload", this.onUnload);

    }

    render(){
        var page = this.props.reducerOutputObject.page
        return (
            <div>
                
                    <Container>
                        <h1 className="mt-5 pt-5 pb-5">
                        <Row>

                            {page.title}
                            </Row>

                        </h1>
                        <h5 className="mt-5">
                        <Row>
                            <Col xs={4}>Einsatzort:</Col><Col xs={8}>
                            {page.location}
                            </Col>
                        </Row>
                        </h5>
                        <h5 className="mt-5">
                        <Row>
                            <Col xs={4}>Einsatzdatum</Col><Col xs={8}>
                            {page.date}
                            </Col>
                        </Row>
                            
                        </h5>
                        <h5 className="mt-5">
                        <Row>
                            <Col xs={4}>Einsatznummer</Col><Col xs={8}>
                        {page.number}
                        </Col>
                        </Row>
                        </h5>
                        {(page.timeOnPage && page.timeOnPage.length) ? (
                        <h5 className="mt-5">
                        <Row>
                            <Col xs={4} className="mt-5">Durchschnittliche Besuchsdauer: </Col><Col  className="mt-5" xs={8}>
                        {console.log("show object")/* {page.timeOnPage.map(time => (<div>{time}</div>))} */}
                        {console.log(page.timeOnPage)}
                        {page.timeOnPage ? page.timeOnPage.map(time => (<div>{time/1000.0}s</div>)): 0}
                        </Col>
                        </Row>
                        </h5>
                        ) :  (<div></div>)  }
                        
                        
                        
                        <Row className="mt-5">
                            <Col xs={4}> <h5>Beschreibung</h5></Col><Col xs={8}>
                            <h5>{page.text} </h5>
                        </Col>
                        </Row>
                        <h5 className="mt-5  mb-5">
                        <Row>
                            <Col xs={4}>ID</Col><Col xs={8}>
                        {page._id}
                        </Col>
                        </Row>
                        </h5>
                        
                        <Button href="/" >Zurück</Button>&nbsp;

                    </Container>
            </div>
        );
    }


}



Pages.propTypes = {
    getPage: PropTypes.func.isRequired,
    reducerOutputObject: PropTypes.object.isRequired,
    reducerOutputObject2: PropTypes.object.isRequired

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
    reducerOutputObject: state.pages,
    reducerOutputObject2: state.search 

    // name because you can access all values with the names/values you see in pageReducer
    // reducerOutputObject: state.reducername

    //Das dort definierte ReducerOutputObject ist eigentlich der aktuelle store-inhalt (state = store), state.pages heißt, dass store.pageReducerValues.dortgespeicherte Objekte
})

export default connect(mapStateToProps,
    {getPage} // redux mapDispatchToProps in short Object-notation-form
)(Pages); // die Klasse