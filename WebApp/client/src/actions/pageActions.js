// axios ist einfach ein HTTP-Client der Daten von unserem Backend gettet
// alternative wäre fetch-api, aber da muss man mit "http://localhost..." usw arbeiten
// -> axios weis wo wir uns befinden

import {GET_PAGES, ADD_PAGE, DELETE_PAGE, PAGES_LOADING} from "./types";
import axios from "axios";

// es handelt sich hier eigentlich um action-creator
// 1 action == 1 Object
// 1 action-creator == 1 Function, die dieses Objekt erzeugt + eventuelle api-calls

// to dispatch = etwas versenden
// das erste dispatch ist ein Funktionsname
// Basically dispatch is used as a callback which gets 
// invoked once some async action is complete. 
// In redux-thunk dispatch is simply a function which dispatches an action to the Redux store after, let's say, you fetch data from an api (which is asynchronous).
export const getPages = () => dispatch => {
    dispatch(setPagesLoading());
    axios
        .get("api/pages")
        .then(response => dispatch({
            type: GET_PAGES,
            payload: response.data
        }))
};

// get called from the pageList.js by the delete Button
// its gonna get send to the reducer zusammen mit dem payload
export const deletePage = (id) => dispatch => {
    axios
        .delete(`/api/pages/${id}`)
        .then(response => dispatch({
            type: DELETE_PAGE,
            payload: id
        }))
};

export const addPage = (page) => dispatch => {
    axios
        .post("/api/pages", page)
        .then(response => dispatch({
            type: ADD_PAGE,
            payload: response.data
        }))
};

export const setPagesLoading = () => {
    return {
        type: PAGES_LOADING
    };
};