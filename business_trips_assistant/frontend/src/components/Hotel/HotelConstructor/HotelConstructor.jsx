import classes from "./HotelConstructor.module.css";
import cn from "classnames";
import {NavLink} from "react-router-dom";
import {useState} from "react";

const HotelConstructor = (props) => {
    return (
        <div className={classes.hotels}>
            <div>
                <div className={classes.name}>
                    {props.name}
                </div>
            </div>
            <div className={classes.centering}>
                <div className={classes.name}>
                    Оценка:
                </div>
                <div className={classes.name}>
                    {props.evaluation}
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
                <a href={props.link} className={classes.button} target="_blank">
                    Забронировать
                </a>
            </div>
        </div>
    );
}

export default HotelConstructor;
