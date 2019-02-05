import {GET_MOSTOFTENSEARCHED} from "./types";
import axios from "axios";


// returns also getReadLonger4Seconds-Results
export const getMostOftenSearched = () => dispatch => {
    axios
        .get("/api/statistics") // api/pages != /api/pages since we start with the url we are currently on with apt/pages
        .then(response => {dispatch({
            type: GET_MOSTOFTENSEARCHED,
            payload: response.data
        }); console.log()})
};
