// bringt alle Reducer zusammen
// wir haben nur pageReducer
// aber z.B. noch error-reducer, auth-reducer, ...

import {combineReducers} from "redux";
import pageReducer from "./pageReducer";
import searchReducer from "./searchReducer";

export default combineReducers({
    pages: pageReducer,
    search: searchReducer,
    
});