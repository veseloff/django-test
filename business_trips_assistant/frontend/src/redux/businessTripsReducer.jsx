import {businessTripsAPI} from "../api/api";

const SET_BT = "BT/SET-BT";
const ADD_BT = "BT/ADD-BT";
const EDIT_BT = "BT/EDIT-BT";
const REMOVE_BT = "BT/REMOVE-BT";

let initialState = {
    nextId: 2,
    businessTrips: []
        /*{
            id: 0,
            name: "Первая командировка",
            fromCity: "Санкт-Петербург",
            toCity: "Москва",
            //begin: new Date(2021, 8, 30),
            //end: new Date(2021, 9, 10),
            begin: "2021-08-30",
            end: "2021-09-10",
            budget: 50000,
            transport: ["поезд", "самолёт"],
            hotel: "Centeral",
            //dateFrom: new Date(2021, 8, 30), //todo: refactor name
            //dateTo: new Date(2021, 9, 9), //todo: refactor name
            dateFrom: "2021-08-30", //todo: refactor name
            dateTo: "2021-09-09", //todo: refactor name
            status: "Завершённая",
        },
        {
            id: 1,
            name: "Командировка столичная",
            fromCity: "Мурманск",
            toCity: "Москва",
            //begin: new Date(2021, 7, 1),
            //end: new Date(2021, 7, 15),
            begin: "2021-07-01",
            end: "2021-07-15",
            budget: 100000,
            transport: ["поезд"],
            hotel: "КОСМОС",
            //dateFrom: new Date(2021, 7, 1),
            //dateTo: new Date(2021, 7, 13),
            dateFrom: "2021-07-01",
            dateTo: "2021-07-13",
            status: "Активная", //todo: or "В процессе" or "Началась"
        },
    ]*/

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

const setBusinessTrips = (items) => ({type: SET_BT, items: items});

export const setBusinessTripsTC = () => async (dispatch) => {
    //dispatch(toggleIsFetching(true));
    const data = await businessTripsAPI.getBusinessTrips();
    //dispatch(toggleIsFetching(false));
    dispatch(setBusinessTrips(data));
    //dispatch(setTotalUsersCount(data.totalCount));
}

export const addBusinessTrip = (businessTrip) => ({type: ADD_BT, businessTrip: businessTrip});
export const editBusinessTrip = (id, businessTrip) => ({type: EDIT_BT, id: id, businessTrip: businessTrip});
export const removeBusinessTrip = (id) => ({type: REMOVE_BT, id: id});

export default BusinessTripsReducer;