import {GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING, SEARCH_RESULTS_LOADING} from "../actions/types";

const initialState = {
    searchResults: [],
    loading: false
}

export default function(state = initialState, action){ 
    switch(action.type){
        case GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING:
        if(action.searchString || (action.dateFROM && action.dateTO)){
            return {
                ...state,
                searchString: action.searchString,
                dateFROM: action.dateFROM,
                dateTO: action.dateTO,
                searchResults: action.payload,
                loading: false
            };}
        else{
            return {
                ...state,
                searchString: action.searchString,
                dateFROM: action.dateFROM,
                dateTO: action.dateTO,
                searchResults: [], // empty searchResults - storage 
                loading: false
            }
        }
        case SEARCH_RESULTS_LOADING:
            return {
                ...state,
                loading: true
            }
        default:
            return state;
    }
    
    
}