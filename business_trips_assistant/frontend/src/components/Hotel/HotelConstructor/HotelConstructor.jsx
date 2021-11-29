import classes from "./HotelConstructor.module.css";
import {useState} from "react";
import Window from "../../Common/Window/Window";

const HotelConstructor = (props) => {
    const [visibility, setVisibility] = useState(false);

    return (
        <div className={classes.hotels}>
            <Window label={`Вы забронировали место в "${props.name}"?`}
                    visibility={visibility} setVisibility={setVisibility} action={props.onBooking}
                    item={props} agree="Да" disagree="Нет"/>
            <div>
                <div className={classes.name}>
                    {props.name}
                </div>
            </div>
            <div>
                <div className={classes.centering}>
                    <div className={classes.name}>
                        Оценка:
                    </div>
                    <div className={classes.name}>
                        {props.evaluation || "Нет оценок"}
                    </div>
                </div>
                <div className={classes.centering}>
                    {props.star !== undefined ? props.star + " звезды" : null}
                </div>
            </div>
            <div className={classes.centering}>
                <div className={classes.name}>
                    Цена:
                </div>
                <div className={classes.name}>
                    {props.price}
                </div>
            </div>
            <div className={classes.centering}>
                <a href={props.link} className={classes.button} target="_blank" rel="noreferrer" onClick={() => {
                    setVisibility(true);
                }}>
                    Забронировать
                </a>
            </div>
        </div>
    );
}

export default HotelConstructor;
