import {GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING,SEARCH_RESULTS_LOADING} from "./types";
import axios from "axios";

export const getSearchResult = (searchString) => dispatch => {
    if(searchString === "" || searchString === undefined){
        return;
    }
    dispatch(setSearchResultsLoading());
    axios
        .get(`/api/searches/${searchString}`)
        .then(response => {dispatch({
            type: GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING,
            searchString: searchString,
            payload: response.data
        }); console.log();
    })
    
};

export const setSearchResultsLoading = () => {
    return {
        type: SEARCH_RESULTS_LOADING
    };
};
