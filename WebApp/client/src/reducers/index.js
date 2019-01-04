// bringt alle Reducer zusammen
// wir haben nur pageReducer
// aber z.B. noch error-reducer, auth-reducer, ...

import {combineReducers} from "redux";
import pageReducer from "./pageReducer";

export default combineReducers({
    page: pageReducer
});