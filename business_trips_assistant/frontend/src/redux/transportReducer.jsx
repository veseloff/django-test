import {transportAPI} from "../api/api";

const SET_TRANSPORT = "TRANSPORT/SET-TRANSPORT";
const SET_DATA = "TRANSPORT/SET-DATA";
const SET_STATIONS_FROM = "TRANSPORT/SET-STATIONS-FROM";
const SET_STATIONS_TO = "TRANSPORT/SET-STATIONS-TO";
const SET_CITY_FROM = "TRANSPORT/SET-CITY-FROM";
const SET_CITY_TO = "TRANSPORT/SET-CITY-TO";
const INITIALIZED_SUCCESS = "TRANSPORT/INITIALIZED-SUCCESS";

let initialState = {
    initialized: false,
    transport: [],
    transportDataSearch: {},
    stationsFrom: [],
    stationsTo: [],
    codeCityFrom: '',
    codeCityTo: '',
}

const TransportReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_TRANSPORT:
            return {...state, transport: [...action.items]};
        case SET_DATA:
            return {...state, transportDataSearch: {...action.items}};
        case SET_STATIONS_FROM:
            return {...state, stationsFrom: [...action.items]};
        case SET_STATIONS_TO:
            return {...state, stationsTo: [...action.items]};
        case SET_CITY_FROM:
            return {...state, codeCityFrom: action.item};
        case SET_CITY_TO:
            return {...state, codeCityTo: action.item};
        case INITIALIZED_SUCCESS:
            return {...state, initialized: true}
        default:
            return state;
    }
}

export const setRZDTC = (info) => async (dispatch) => {
    const data = await transportAPI.getRZD(info.cityT, info.cityF, info.stationT, info.stationF, info.codeST, info.codeSF, info.date);
    if (data !== undefined) {
        dispatch(setTransport(data));
        dispatch(setTransportDataSearch(info));
    }
}

export const initializeTransport = (cityFrom, cityTo) => (dispatch) => {
    const isDoneSetStationsFrom = dispatch(setStationsTC(cityFrom, true));
    const isDoneSetStationsTo = dispatch(setStationsTC(cityTo, false));
    Promise.all([isDoneSetStationsFrom, isDoneSetStationsTo]).then(() => dispatch(initializedSuccess()));
}

export const setStationsTC = (city, from) => async (dispatch) => {
    const data = await transportAPI.getCodeCity(city)
    if (data !== undefined) {
        dispatch(setCodeCity(from ? SET_CITY_FROM : SET_CITY_TO, data[0].cityCode));
        await transportAPI.getStations(data[0].cityCode)
            .then(response => {
                dispatch(setStations(from ? SET_STATIONS_FROM : SET_STATIONS_TO, response));
            })
    }
}

const initializedSuccess = () => ({type: INITIALIZED_SUCCESS});
const setTransport = (items) => ({type: SET_TRANSPORT, items});
const setTransportDataSearch = (items) => ({type: SET_DATA, items});
const setStations = (type, items) => ({type: type, items});
const setCodeCity = (type, item) => ({type: type, item});

export default TransportReducer;