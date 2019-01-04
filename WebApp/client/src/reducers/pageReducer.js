// Was passiert hier? der PageReducer stellt Methoden bereit, um den internal state zu manipulieren

import {GET_PAGES, ADD_PAGE, DELETE_PAGE, PAGES_LOADING} from "../actions/types";

var date = new Date();

const initialState = {
    pages: [],
    // reason: fetch data needs a couple milliseconds. Then we get data, this will be set to true and if finished again to false
    // während loading true ist kann man dann einen spinner o.ä. hinzufügen ...
    loading: false
}

// public methods zum manipulieren des states
// state = initialState wird benötigt, da wir selbst ja nie den reducer aufrufen, aber der store schon
// und wenn der store seinen state(store-intern) an state(parameter) übergeben möchte, aber noch 
// keinen state hat (gerade initialisiert) wird der hier definierte initialState genommen
// wir können eigentlich nur die action beeinflussen, die der store an den reducer übergibt, den 
// state parameter macht er selbst
export default function(state = initialState, action){ // diese 2 Parameter müssen genau so heißen und sind nicht optional
    switch(action.type){
        // returns the state from the store
        case GET_PAGES:
            return {
                ...state,
                pages: action.payload, // kopiert den initial state und fügt die pages aus der Datenbank hinzu
                loading: false // at the start of the request we set loading to true
            };
        // get called from the action deletePage (which is triggert from pageList.js)
        case DELETE_PAGE:
            return {
                ...state, // initial state
                pages: state.pages.filter(page => page._id !== action.payload)

            };
        case ADD_PAGE:
            return {
                ...state,
                pages: [action.payload, ...state.pages]
            };
        case PAGES_LOADING:
            return {
                ...state,
                loading: true
            }
        default:
            return state;
    }
    
    
}