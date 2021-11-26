import {applyMiddleware, combineReducers, compose, createStore} from "redux";
import BusinessTripsReducer from "./businessTripsReducer";
import hotelReducer from "./hotelReducer";
import thunkMiddleware from "redux-thunk";
//import {reducer as formReducer} from "redux-form";

const reducers = combineReducers({
    businessTripsData: BusinessTripsReducer,
    hotelsData: hotelReducer,
});


const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
export default createStore(reducers, composeEnhancers(applyMiddleware(thunkMiddleware)));