import {GET_READTIME} from "./types";
import axios from "axios";

export const getReadTime = () => dispatch => {
    axios
        .get("/api/statistics") // api/pages != /api/pages since we start with the url we are currently on with apt/pages
        .then(response => {dispatch({
            type: GET_READTIME,
            payload: response.data
        }); console.log()})
};
