import uuid from "uuid";
import {GET_PAGES, ADD_PAGE, DELETE_PAGE} from "../actions/types";

var date = new Date();

const initialState = {
    pages: [
        {id: uuid(), date: (date.getDay()-1).toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),title: "test1",location: "test123",text: "text123",number: ["1234",""]},

        {id: uuid(), date: (date.getDay()-1).toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),title: "test2",location: "test123",text: "text123",number: ["1234",""]},

        {id: uuid(), date: (date.getDay()-1).toString() + "." + (date.getMonth() + 1).toString() + "." + date.getFullYear().toString(),title: "test3",location: "test123",text: "text123",number: ["1234",""]}
    ]
}

export default function(state = initialState, action){
    switch(action.type){
        case GET_PAGES:
            return {
                ...state
            }
        default:
            return state;
    }
}