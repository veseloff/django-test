import classes from "./ExpensesConstructor.module.css";
import cn from "classnames";
import {NavLink} from "react-router-dom";
import {useState} from "react";
import Window from "../../Common/Window/Window";

const ExpensesConstructor = (props) => {
    const dateTime = props.expenses.datetime.split(' ');
    const date = dateTime[0].replace(/-/g, "." );
    const time = dateTime[1].split(':');
    return (
        <div className={classes.business_trip}>
            <div>
                <div>
                    {props.expenses.report.split('* ').map((s, i) => <div>{s}</div> )}
                </div>
            </div>
            <div>
                <div>
                    Сумма: {props.expenses.summary || "Неизвестно"} р
                </div>
            </div>
            <div>
                <div>
                    {date}
                </div>
                <div>
                    {time[0] + ':' + time[1]}
                </div>
            </div>
        </div>
    );
}

export default ExpensesConstructor;
