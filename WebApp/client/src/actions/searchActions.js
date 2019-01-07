import {GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING,SEARCH_RESULTS_LOADING} from "./types";
import axios from "axios";

export const getSearchResult = (searchStringWithDate) => dispatch => {
    dispatch(setSearchResultsLoading());
    if(searchStringWithDate.searchString || (searchStringWithDate.dateFROM && searchStringWithDate.dateTO))
{    
    console.log("lll");
    console.log(searchStringWithDate);
    
    axios
        .get("/api/searches", {params: {
            searchString: searchStringWithDate.searchString,
            dateFROM: searchStringWithDate.dateFROM,
            dateTO: searchStringWithDate.dateTO
        }})
        .then(response => {dispatch({
            type: GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING,
            searchString: searchStringWithDate.searchString,
            dateFROM: searchStringWithDate.dateFROM,
            dateTO: searchStringWithDate.dateTO,
            payload: response.data
        }); console.log();
    })}
    else{
        console.log("hiiiieeerrr");
        var returnStatement = {
            type: GET_SEARCH_RESULT_WITH_GIVEN_SEARCHSTRING,
            searchString: searchStringWithDate,
        };
        dispatch(returnStatement);
    }
    
};

export const setSearchResultsLoading = () => {
    return {
        type: SEARCH_RESULTS_LOADING
    };
};
