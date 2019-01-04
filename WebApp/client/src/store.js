import {createStore, applyMiddleware, compose} from "redux";
 // 1 layer des middlewares
 // gibt die Möglichkeit anders als normal asynchronous calles von den action-creators zu den
 // Servern zu machen
import thunk from "redux-thunk";
import rootReducer from "./reducers"; // calles /reducers/index.js per default

const initialState = {};

const middleware = [thunk];

const store = createStore(rootReducer, initialState, compose( // compose fügt mehrere middlewares zusammen

    // spread - operator: use Array - elements as function - parameters
    applyMiddleware(...middleware),
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()

));

export default store;