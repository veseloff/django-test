import {businessTripsAPI} from "../api/api";
import Cookies from 'js-cookie';

const SET_BTs = "BT/SET-BTs";
const SET_BT = "BT/SET-BT";
const SET_ID = "BT/SET-ID";
const INITIALIZED_SUCCESS = "BT/INITIALIZED-SUCCESS";
const UNINITIALIZED_SUCCESS = "BT/UNINITIALIZED-SUCCESS";

let initialState = {
    initialized: false,
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
        case INITIALIZED_SUCCESS:
            return {...state, initialized: true}
        case UNINITIALIZED_SUCCESS:
            return {...state, initialized: false}
        default:
            return state;
    }
}

export const setBusinessTripsTC = (userId) => async (dispatch) => {
    const data = await businessTripsAPI.getBusinessTrips(userId);
    if (data !== undefined)
        dispatch(setBusinessTrips(data));
}

export const setBusinessTripInfoTC = (id) => async (dispatch) => {
    const data = await businessTripsAPI.getBusinessTripInfo(id);
    if (data !== undefined)
        dispatch(setBusinessTripInfo({...data.businessTrip, hotel: {...data.hotel}, trip: [...data.trip]}));
}

export const postBusinessTripsTC = (bt) => async (dispatch) => {
    await businessTripsAPI.postBusinessTrips(bt).then(result => {
        dispatch(setBusinessTripId(result));
    });
}

export const putBusinessTripsTC = (idBT, bt) => async (dispatch) => {
    await businessTripsAPI.putBusinessTrips(idBT, bt);
}

export const deleteBusinessTripsTC = (userId, id) => async (dispatch) => {
    await businessTripsAPI.deleteBusinessTrips(id).then(() => {
        dispatch(setBusinessTripsTC(userId));
    });
}

export const postHotelInfoTC = (info) => async (dispatch) => {
    await businessTripsAPI.postHotelInfo(info).then(() => {
        dispatch(setBusinessTripInfo({hotel: info}));
    });
}

export const putHotelInfoTC = (info) => async (dispatch) => {
    await businessTripsAPI.putHotelInfo(info)
}

export const initializeBTInfo = (id) => (dispatch) => {
    if (id !== 'new') {
        const isDone = dispatch(setBusinessTripInfoTC(id));
        Promise.all([isDone]).then(() => dispatch(initializedSuccess()));
    } else
        dispatch(initializedSuccess())
}

const initializedSuccess = () => ({type: INITIALIZED_SUCCESS});
export const uninitializedSuccess = () => ({type: UNINITIALIZED_SUCCESS});
export const setBusinessTrips = (items) => ({type: SET_BTs, items: items});
const setBusinessTripInfo = (items) => ({type: SET_BT, items: items});
const setBusinessTripId = (item) => ({type: SET_ID, item: item});

export default BusinessTripsReducer;