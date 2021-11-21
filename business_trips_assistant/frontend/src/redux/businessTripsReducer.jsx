import {businessTripsAPI} from "../api/api";
import Cookies from 'js-cookie';

const SET_BTs = "BT/SET-BTs";
const SET_BT = "BT/SET-BT";
const SET_ID = "BT/SET-ID";
const ADD_BT = "BT/ADD-BT";
const EDIT_BT = "BT/EDIT-BT";
const REMOVE_BT = "BT/REMOVE-BT";

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
        case ADD_BT:
            return {...state, businessTrips: [...state.businessTrips, action.businessTrip]};
        case EDIT_BT:
            let index = -1;
            state.businessTrips.find((bt, i) => {
                if (bt.id === action.id) {
                    index = i;
                    return true;
                }
                return false;
            })
            if (index !== -1) {
                let newBusinessTrips = state.businessTrips.slice();
                newBusinessTrips[index] = action.businessTrip;
                return {
                    ...state,
                    businessTrips: newBusinessTrips,
                };
            }
            return state;
        case REMOVE_BT:
            return {...state, businessTrips: state.businessTrips.filter(bt => bt.id !== action.id)};
        default:
            return state;
    }
}

export const setBusinessTripsTC = () => async (dispatch) => {
    const data = await businessTripsAPI.getBusinessTrips();
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

export const putBusinessTripsTC = () => async (dispatch) => {
    //dispatch(toggleIsFetching(true));
    const data = await businessTripsAPI.postBusinessTrips();
    //dispatch(toggleIsFetching(false));
    dispatch(editBusinessTrip(data));
}

export const deleteBusinessTripsTC = (id) => async (dispatch) => {
    const data = await businessTripsAPI.getCsrf();
    if (data !== undefined) {
        dispatch(() => Cookies.set('csrftoken', data));
        businessTripsAPI.deleteBusinessTrips(id).then(result => console.log(result));
    }
}

const setBusinessTrips = (items) => ({type: SET_BTs, items: items});
const setBusinessTrip = (items) => ({type: SET_BT, items: items});
const setBusinessTripId = (item) => ({type: SET_ID, item: item});
const addBusinessTrip = (businessTrip) => ({type: ADD_BT, businessTrip: businessTrip});
export const editBusinessTrip = (id, businessTrip) => ({type: EDIT_BT, id: id, businessTrip: businessTrip});
export const removeBusinessTrip = (id) => ({type: REMOVE_BT, id: id});

export default BusinessTripsReducer;