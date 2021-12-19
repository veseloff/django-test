import classes from "./TransportConstructor.module.css";
import {useState} from "react";
import Window from "../../Common/Window/Window";

const TransportConstructor = (props) => {
    const [visibility, setVisibility] = useState(false);

    const convertTime = (time) => {
        if (time !== undefined) {
            const parseTime = time.split(":");
            if (parseTime.length === 2) {
                const day = Math.floor(parseTime[0] / 24)
                return `${day !== 0 ? day + ' д' : ''} ${parseTime[0] % 24} ч ${parseTime[1]} м`;
            }
            return time;
        }
    };

    return (
        <div className={classes.business_trip}>
            <Window label={`Вы купили билет на поезд "${props.trip.number}"?`}
                    visibility={visibility} setVisibility={setVisibility} action={props.onBuying}
                    item={props} agree="Да" disagree="Нет"/>
            <div>
                <div className={classes.name}>
                    {props.trip.number} {props.transportDataSearch.cityF} - {props.transportDataSearch.cityT}
                </div>
            </div>
            <div>
                <div className={classes.name}>
                    {props.trip.localTime0} ({props.trip.timeDeltaString0})
                </div>
                <div>
                    {props.trip.localDate0}
                </div>
                <div>
                    {props.trip.station0}
                </div>
            </div>
            <div className={classes.centering}>
                <div>
                    {convertTime(props.trip.timeInWay)}
                </div>
            </div>
            <div>
                <div className={classes.name}>
                    {props.trip.localTime1} ({props.trip.timeDeltaString1})
                </div>
                <div>
                    {props.trip.localDate1}
                </div>
                <div>
                    {props.trip.station1}
                </div>
            </div>
            <div className={classes.centering}>
                <a href={props.trip.link} className={classes.button} target="_blank" rel="noreferrer"onClick={() => {
                    setVisibility(true);
                }}>
                   Купить билет
                </a>
            </div>
        </div>
    );
}

export default TransportConstructor;
