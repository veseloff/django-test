import {authAPI, businessTripsAPI} from "../api/api";
import Cookies from "js-cookie";
import {setBusinessTrips} from "./businessTripsReducer";

const SET_USER_DATA = "auth/SET_USER_DATA";
const SET_PROFILE = "auth/SET_PROFILE";

let initialState = {
    userId: null,
    email: null,
    username: null,
    isAuth: false,
    isFetching: false,
}

const AuthReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_USER_DATA:
            return {...state, userId: action.userId, isAuth: action.isAuth, username: action.username};
        case SET_PROFILE:
            return {...state, ...action.data};
        default:
            return state;
    }
}

const setUserId = (userId, isAuth, username) => ({type: SET_USER_DATA, userId, isAuth, username});
const setProfileData = (data) => ({type: SET_PROFILE, data});

export const postAuthLoginTC = (info) => async (dispatch) => {
    const dataCsrf = await authAPI.getCsrf();
    if (dataCsrf !== undefined) {
        dispatch(() => Cookies.set('csrftoken', dataCsrf));
        const data = await authAPI.postAuthLogin(info)
        dispatch(setUserId(data, true, info.username));
        const newDataCsrf = await authAPI.getCsrf();
        if (newDataCsrf !== undefined) {
            dispatch(() => Cookies.set('csrftoken', newDataCsrf));
        }
    }
}

export const deleteAuthLoginTC = () => async (dispatch) => {
    const data = await authAPI.deleteAuthLogin();
    dispatch(setUserId(null, false, null));
    dispatch(setBusinessTrips([]))
}

export default AuthReducer;