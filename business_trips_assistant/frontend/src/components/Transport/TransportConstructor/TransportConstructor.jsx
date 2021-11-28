import classes from "./TransportConstructor.module.css";
import {NavLink} from "react-router-dom";
import {useState} from "react";

const TransportConstructor = (props) => {
    const [visibility, setVisibility] = useState(false);

    const convertDate = (date) => {
        if (date !== undefined) {
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
                    777А Санкт-Петербург - Москва
                </div>
            </div>
            <div>
                <div className={classes.name}>
                    19:10
                </div>
                <div>
                    30.09.2021
                </div>
                <div>
                    Московский вокзал
                </div>
            </div>
            <div className={classes.centering}>
                <div>
                    4 ч 5 мин
                </div>
            </div>
            <div>
                <div className={classes.name}>
                    23:15
                </div>
                <div>
                    30.09.2021
                </div>
                <div>
                    Ленинградский вокзал
                </div>
            </div>
            <div className={classes.centering}>
                <NavLink to={`#`} className={classes.button}>
                    Купить билет
                </NavLink>
            </div>
        </div>
    );
}

export default TransportConstructor;
