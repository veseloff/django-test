import {applyMiddleware, combineReducers, compose, createStore} from "redux";
import BusinessTripsReducer from "./businessTripsReducer";
import hotelReducer from "./hotelReducer";
import AppReducer from "./appReducer";
import AuthReducer from "./authReducer";
import thunkMiddleware from "redux-thunk";
import ExpensesReducer from "./expensesReducer";

const reducers = combineReducers({
    businessTripsData: BusinessTripsReducer,
    expensesData: ExpensesReducer,
    hotelsData: hotelReducer,
    app: AppReducer,
    auth: AuthReducer,
});


const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
export default createStore(reducers, composeEnhancers(applyMiddleware(thunkMiddleware)));