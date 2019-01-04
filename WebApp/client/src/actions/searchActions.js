import {GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING,SEARCH_RESULTS_LOADING} from "./types";
import axios from "axios";

export const getSearchResult = (searchString) => dispatch => {
    dispatch(setSearchResultsLoading());
    axios
        //.get(`/${searchString}`)
        .get(`/api/searches/${searchString}`)
        .then(response => {dispatch({
            type: GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING,
            searchString: searchString,
            payload: response.data
        }); console.log(searchString); console.log(response);
    })
    
};

export const setSearchResultsLoading = () => {
    return {
        type: SEARCH_RESULTS_LOADING
    };
};
