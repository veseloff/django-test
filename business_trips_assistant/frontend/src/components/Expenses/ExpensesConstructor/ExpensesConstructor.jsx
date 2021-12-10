import classes from "./ExpensesConstructor.module.css";
import cn from "classnames";
import {NavLink} from "react-router-dom";
import {useState} from "react";
import Window from "../../Common/Window/Window";

const ExpensesConstructor = (props) => {
    const convertDate = (date) => {
        if (!(date === undefined || date === 'None')) {
            const parseDate = date.split("-");
            if (parseDate.length === 3)
                return `${parseDate[2]}.${parseDate[1]}.${parseDate[0]}`;
            return date;
        }
    };

    return (
        <div className={classes.business_trip}>
            <div>
                <div className={classes.name}>
                    {props.expenses.name}
                </div>
                <div>
                    Сумма: {props.expenses.summary || "Неизвестно"}р
                </div>
            </div>
            <div>
                <div className={classes.name}>
                    {props.expenses.time}
                </div>
                <div>
                    {convertDate(props.expenses.date) || "Неизвестно"}
                </div>
            </div>
        </div>
    );
}

export default ExpensesConstructor;
