import classes from "./BusinessTripConstructor.module.css";
import cn from "classnames";
import {NavLink} from "react-router-dom";
import {useState} from "react";
import Window from "../../Common/Window/Window";

const BusinessTripConstructor = (props) => {
    const [visibility, setVisibility] = useState(false);

    const convertDate = (date) => {
        if (!(date === undefined || date === 'None')) {
            return date.replace(/-/g, ".")
        }
    };

    return (
        <div className={classes.business_trip}>
            <Window label={`Вы уверенны, что хотите удалить командировку "${props.businessTrip.name}"?`}
                    visibility={visibility} setVisibility={setVisibility} action={props.onDelete}
                    item={props.businessTrip.id} agree="Удалить" disagree="Отмена"/>
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
                <div>
                    Бюджет: {props.businessTrip.budget || "Неизвестно"}р
                </div>
            </div>
            <div>
                С {convertDate(props.businessTrip.begin) || "Неизвестно"} по {convertDate(props.businessTrip.end) || "Неизвестно"}
            </div>
            <div>
                <div>
                    Отель: {props.businessTrip.hotel || "Неизвестно"}
                </div>
            </div>
            <div>
                {
                    props.businessTrip.transport?.length !== 0
                        ? <div className={classes.trip}>
                            Транспорт: {props.businessTrip.transport?.map((t, index) =>
                            <div className={cn(classes.icon, {
                                [classes.airplane]: t === "Самолёт",
                                [classes.train]: t === "Поезд",
                            })} key={index}/>)} {/*todo: add icon*/}
                        </div>
                        : null
                }
                <div>
                    Туда: {convertDate(props.businessTrip.dateDeparture0) || "Неизвестно"}
                </div>
                <div>
                    Обратно: {convertDate(props.businessTrip.dateDeparture1) || "Неизвестно"}
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
