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
    console.log(data);
    if (data !== undefined)
        dispatch(setExpensesData(data.reportShort, data.reportFull));
}

const setExpensesData = (fullExpenses, lastExpenses) => ({type: SET_DATA, fullExpenses, lastExpenses});

export default ExpensesReducer;