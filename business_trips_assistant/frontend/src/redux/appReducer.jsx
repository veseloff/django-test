import {postAuthLoginTC} from "./authReducer";


const INITIALIZED_SUCCESS = "APP/INITIALIZED-SUCCESS";

const initialState = {
    initialized: false,
}

const AppReducer = (state = initialState, action) => {
    switch (action.type) {
        case INITIALIZED_SUCCESS:
            return {...state, initialized: true}
        default:
            return state;
    }
}

const initializedSuccess = () => ({type: INITIALIZED_SUCCESS});

export const initializeApp = () => (dispatch) => {
    const authMe = dispatch(postAuthLoginTC());
    Promise.all([authMe]).then(() => dispatch(initializedSuccess()));
}

export default AppReducer;