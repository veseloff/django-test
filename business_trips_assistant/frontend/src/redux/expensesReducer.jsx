let initialState = {
    fullExpensesData: [
        {
            date: "07.12.2021",
            "Рублей": 122,
        },
        {
            date: "08.12.2021",
            "Рублей": 704,
        },
        {
            date: "09.12.2021",
            "Рублей": 1909,
        },
        {
            date: "10.12.2021",
            "Рублей": 700,
        },
        {
            date: "11.12.2021",
            "Рублей": 152,
        },
        {
            date: "12.12.2021",
            "Рублей": 1670,
        },
        {
            date: "13.12.2021",
            "Рублей": 2000,
        }
    ],
    lastExpensesData: [
        {
            name: ["Телефон"],
            summary: 62488.00,
            date: "11.12.2021",
            time: "12:00",
        },
        {
            name: ["Еда"],
            summary: 3288.10,
            date: "12.12.2021",
            time: "18:00",
        },
        {
            name: ["Шава"],
            summary: 128.00,
            date: "13.12.2021",
            time: "12:00",
        },
        {
            name: ["Чехол"],
            summary: 2488.00,
            date: "13.12.2021",
            time: "13:00",
        },
    ],
}

const ExpensesReducer = (state = initialState, action) => {
    switch (action.type) {
        default:
            return state;
    }
}

export default ExpensesReducer;