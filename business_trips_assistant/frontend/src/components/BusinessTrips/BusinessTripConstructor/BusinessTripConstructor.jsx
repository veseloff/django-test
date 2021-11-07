import classes from "./BusinessTripConstructor.module.css";
import cn from "classnames";
import {NavLink} from "react-router-dom";
import {useState} from "react";

const BusinessTripConstructor = (props) => {
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
            <div className={cn(classes.delete_wrapper, {
                [classes.hidden]: !visibility,
                [classes.visible]: visibility,
            })}>
                <div className={classes.delete_container}>
                    <div>Вы уверенны, что хотите удалить командировку "{props.businessTrip.name}"?</div>
                    <div className={classes.button_wrapper}>
                        <button className={cn(classes.button, classes.delete)} onClick={() => {
                            props.onDelete(props.businessTrip.id);
                            setVisibility(false)
                        }}>
                            Удалить
                        </button>
                        <button className={classes.button} onClick={() => {
                            setVisibility(false)
                        }}>Отмена
                        </button>
                    </div>
                </div>
            </div>
            <div>
                <div className={classes.name}>
                    {props.businessTrip.name}
                </div>
                <div>
                    {props.businessTrip.fromCity} - {props.businessTrip.toCity}
                </div>
                <div>
                    Статус: {props.businessTrip.status || "Неизвестно"}
                </div>
            </div>
            <div>
                С {convertDate(props.businessTrip.begin) || "Неизвестно"} по {convertDate(props.businessTrip.end) || "Неизвестно"}
            </div>
            <div>
                <div>
                    Транспорт: {props.businessTrip.transport.join(", ")} {/*todo: add icon*/}
                </div>
                <div>
                    Отель: {props.businessTrip.hotel} {/*todo: add break-word (https://css-live.ru/articles/gde-vsyo-slozhno-s-perenosami-strok-vot-vse-css-i-html-xitrosti-dlya-etogo.html)*/}
                </div>
            </div>
            <div>
                <div>
                    Туда: {convertDate(props.businessTrip.dateFrom) || "Неизвестно"}
                </div>
                <div>
                    Обратно: {convertDate(props.businessTrip.dateTo) || "Неизвестно"}
                </div>
            </div>
            <div className={classes.button_container}>
                <div>
                    <button className={cn(classes.button, classes.delete_button, classes.delete)} onClick={() => {
                        setVisibility(true);
                    }}>
                        X
                    </button>
                </div>
                <NavLink to={`/business-trips/${props.businessTrip.id}`} className={classes.button}>
                    Открыть
                </NavLink>
            </div>
        </div>
    );
}

export default BusinessTripConstructor;
