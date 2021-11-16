import {businessTripsAPI} from "../api/api";
import Cookies from 'js-cookie';

const SET_BT = "BT/SET-BT";
const ADD_BT = "BT/ADD-BT";
const EDIT_BT = "BT/EDIT-BT";
const REMOVE_BT = "BT/REMOVE-BT";

let initialState = {
    nextId: 2,
    businessTrips: []
}

const BusinessTripsReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_BT:
            return {...state, businessTrips: [...action.items]};
        case ADD_BT:
            return {...state, nextId: state.nextId + 1, businessTrips: [...state.businessTrips, action.businessTrip]};
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
    dispatch(setBusinessTrips(data));
}

export const setCsrfTC = () => async (dispatch) => {
    const data = await businessTripsAPI.getCsrf();
    console.log(data);
    dispatch(() => Cookies.set('csrftoken', data));
}

export const postBusinessTripsTC = (bt) => async (dispatch) => {
    bt = {
        user_id: 1,
        date_start: "2021-10-24",
        credit: 50000,
        date_finish: "2021-11-06",
        from_city: "Екатеринбург",
        hotel: "КОСМОС",
        id: 2,
        name: "Столичная командировка",
        to_city: "Москва",
        transport: ['Самолёт', 'Поезд'],
    }
    console.log(bt)
    const data = await businessTripsAPI.getCsrf();
    dispatch(() => Cookies.set('csrftoken', data));
    businessTripsAPI.postBusinessTrips(bt).then(result => console.log(result));                      //todo: VsALT - вызов post запроса
}

export const putBusinessTripsTC = () => async (dispatch) => {
    //dispatch(toggleIsFetching(true));
    const data = await businessTripsAPI.postBusinessTrips();
    //dispatch(toggleIsFetching(false));
    dispatch(editBusinessTrip(data));
}

export const deleteBusinessTripsTC = () => async (dispatch) => {
    //dispatch(toggleIsFetching(true));
    const data = await businessTripsAPI.postBusinessTrips();
    //dispatch(toggleIsFetching(false));
    dispatch(removeBusinessTrip(data));
}

const setBusinessTrips = (items) => ({type: SET_BT, items: items});
const addBusinessTrip = (businessTrip) => ({type: ADD_BT, businessTrip: businessTrip});
export const editBusinessTrip = (id, businessTrip) => ({type: EDIT_BT, id: id, businessTrip: businessTrip});
export const removeBusinessTrip = (id) => ({type: REMOVE_BT, id: id});

export default BusinessTripsReducer;