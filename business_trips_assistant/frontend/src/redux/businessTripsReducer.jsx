import {businessTripsAPI} from "../api/api";
import Cookies from 'js-cookie';

const SET_BTs = "BT/SET-BTs";
const SET_BT = "BT/SET-BT";
const SET_ID = "BT/SET-ID";

let initialState = {
    businessTrips: [],
    businessTrip: {},
}

const BusinessTripsReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_BTs:
            return {...state, businessTrips: [...action.items], businessTrip: {}};
        case SET_BT:
            return {...state, businessTrip: {...state.businessTrip, ...action.items}};
        case SET_ID:
            return {...state, businessTrip: {...state.businessTrip, id: action.item}};
        default:
            return state;
    }
}

export const setBusinessTripsTC = () => async (dispatch) => {
    const data = await businessTripsAPI.getBusinessTrips(2);
    if (data !== undefined)
        dispatch(setBusinessTrips(data));
}

export const setCsrfTC = () => async (dispatch) => {
    const data = await businessTripsAPI.getCsrf();
    console.log(data);
    dispatch(() => Cookies.set('csrftoken', data));
}

export const postBusinessTripsTC = (bt) => async (dispatch) => {
    const dataCsrf = await businessTripsAPI.getCsrf();
    if (dataCsrf !== undefined) {
        dispatch(() => Cookies.set('csrftoken', dataCsrf));
        await businessTripsAPI.postBusinessTrips(bt).then(result => {
            dispatch(setBusinessTripId(result));
        });
    }
}

export const putBusinessTripsTC = (idBT, bt) => async (dispatch) => {
    const dataCsrf = await businessTripsAPI.getCsrf();
    if (dataCsrf !== undefined) {
        dispatch(() => Cookies.set('csrftoken', dataCsrf));
        await businessTripsAPI.putBusinessTrips(idBT, bt)
    }
}

export const deleteBusinessTripsTC = (id) => async (dispatch) => {
    const data = await businessTripsAPI.getCsrf();
    if (data !== undefined) {
        dispatch(() => Cookies.set('csrftoken', data));
        await businessTripsAPI.deleteBusinessTrips(id).then(() => {
            dispatch(setBusinessTripsTC());
        });
    }
}

const setBusinessTrips = (items) => ({type: SET_BTs, items: items});
const setBusinessTrip = (items) => ({type: SET_BT, items: items});
const setBusinessTripId = (item) => ({type: SET_ID, item: item});

export default BusinessTripsReducer;