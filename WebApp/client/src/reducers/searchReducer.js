import {GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING, SEARCH_RESULTS_LOADING} from "../actions/types";

const initialState = {
    searchResults: [],
    loading: false
}

export default function(state = initialState, action){ 
    switch(action.type){
        case GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING:
            return {
                ...state,
                searchString: action.searchString,
                searchResults: action.payload,
                loading: false
            };
        case SEARCH_RESULTS_LOADING:
            return {
                ...state,
                loading: true
            }
        default:
            return state;
    }
    
    
}