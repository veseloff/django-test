import {expensesAPI} from "../api/api";

const SET_DATA = "EXPENSES/SET-DATA";

let initialState = {
    fullExpensesData: [],
    lastExpensesData: [],
}

const ExpensesReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_DATA:
            return {...state, fullExpensesData: [...action.fullExpenses], lastExpensesData: [...action.lastExpenses]};
        default:
            return state;
    }
}

export const setExpensesDataTC = (idBT) => async (dispatch)  => {
    const data = await expensesAPI.getExpenses(idBT);
    if (data !== undefined) {
        const fullExpenses = data.reportShort.sort((a, b) => new Date(a.date) - new Date(b.date));
        const lastExpenses = data.reportFull.sort((a, b) => new Date(b.datetime) - new Date(a.datetime));
        dispatch(setExpensesData(fullExpenses, lastExpenses));
    }
}

const setExpensesData = (fullExpenses, lastExpenses) => ({type: SET_DATA, fullExpenses, lastExpenses});

export default ExpensesReducer;