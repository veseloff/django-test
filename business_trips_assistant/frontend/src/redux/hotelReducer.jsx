import {hotelsAPI} from "../api/api";

const SET_HOTEL = "HOTEL/SET-HOTEL";
const SET_DATA = "HOTEL/SET-DATA";

let initialState = {
    count: 0,
    hotels: [],
    hotelsDataSearch: {},
}

const HotelReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_HOTEL:
            return {...state, hotels: [...action.items], count: action.count};
        case SET_DATA:
            return {...state, hotelsDataSearch: {...action.items}};
        default:
            return state;
    }
}

export const setHotelsTC = (info) => async (dispatch) => {
    const data = await hotelsAPI.getHotels(info.city, info.offset, info.star, info.option, info.checkIn, info.checkOut);
    if (data !== undefined) {
        dispatch(setHotels(data.count_hotels, data.hotels));
        dispatch(setHotelsDataSearch(info));
    }
}

const setHotels = (count, items) => ({type: SET_HOTEL, count, items});
const setHotelsDataSearch = (items) => ({type: SET_DATA, items});

export default HotelReducer;