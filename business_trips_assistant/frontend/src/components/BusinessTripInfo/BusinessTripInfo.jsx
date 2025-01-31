import {NavLink, withRouter} from "react-router-dom";
import classes from "./BusinessTripInfo.module.css";
import {compose} from "redux";
import {connect} from "react-redux";
import {
    postBusinessTripsTC,
    putBusinessTripsTC,
    setBusinessTripInfoTC, initializeBTInfo
} from "../../redux/businessTripsReducer";
import BusinessTripInfoForm from "./BusinessTripInfoForm/BusinessTripInfoForm";
import {useEffect} from "react";

const BusinessTripInfo = (props) => {
    const id = isNaN(Number(props.match.params.businessTripId))
        ? (props.businessTrip.id || 'new')
        : Number(props.match.params.businessTripId);

    useEffect(() => {
            props.initializeBTInfo(id);
        },
        // eslint-disable-next-line
        []);

    if (!props.initialized)
        return null

    const map = new Map();
    map.set(0, "Самолёт");
    map.set(1, "Поезд");

    const firstTrip = props.businessTrip.trip !== undefined
        ? props.businessTrip.trip.find(trip => trip.isFirst === 0)
        : undefined;
    const secondTrip = props.businessTrip.trip !== undefined
        ? props.businessTrip.trip.find(trip => trip.isFirst === 1)
        : undefined;

    const convertDate = (date) => {
        if (!(date === undefined || date === 'None')) {
            const parseDate = date.split("-");
            if (parseDate.length === 3)
                return `${parseDate[2]}.${parseDate[1]}.${parseDate[0]}`;
            return date;
        }
    };

    const firstTripPrice = firstTrip === undefined ? 0 : firstTrip.priceTicket;
    const secondTripPrice = secondTrip === undefined ? 0 : secondTrip.priceTicket;

    return (
        <div className={classes.body_container}>
            <BusinessTripInfoForm {...props} id={id}/>
            {
                id !== 'new'
                    ? <div className={classes.body_wrapper}>
                        <div className={classes.board_container}>
                            <div className={classes.header}>
                                Транспорт
                            </div>
                            {
                                firstTrip === undefined
                                    ? <NavLink to={`/business-trips/${id}/transport/there`}>Туда: Выбрать...</NavLink>
                                    : <div className={classes.option}>
                                        <div>
                                            Туда:
                                            <div className={classes.description}>
                                                <div>{map.get(firstTrip.transport)} {firstTrip.transportNumber}</div>
                                                <div>{firstTrip.cityFrom} - {firstTrip.cityTo}</div>
                                                <div>
                                                    {convertDate(firstTrip.dateDeparture)} - {convertDate(firstTrip.dateArrival)}
                                                </div>
                                            </div>
                                        </div>
                                        <NavLink to={`/business-trips/${id}/transport/there`}>Изменить...</NavLink>
                                    </div>

                            }
                            {
                                secondTrip === undefined
                                    ? <NavLink to={`/business-trips/${id}/transport/back`}>Обратно: Выбрать...</NavLink>
                                    : <div className={classes.option}>
                                        <div>
                                            Обратно:
                                            <div className={classes.description}>
                                                <div>{map.get(secondTrip.transport)} {secondTrip.transportNumber}</div>
                                                <div>{secondTrip.cityTo} - {secondTrip.cityFrom}</div>
                                                <div>
                                                    {convertDate(secondTrip.dateDeparture)} - {convertDate(secondTrip.dateArrival)}
                                                </div>
                                            </div>
                                        </div>
                                        <NavLink to={`/business-trips/${id}/transport/back`}>Изменить...</NavLink>
                                    </div>
                            }
                            <div className={classes.footer}>
                                Общий расход:
                                {
                                    ' ' + (firstTripPrice + secondTripPrice) + " руб"
                                }
                            </div>
                        </div>
                        <div className={classes.board_container}>
                            <div className={classes.header}>
                                Отель
                            </div>
                            {
                                props.businessTrip?.hotel?.name === undefined
                                    ? <div>
                                        Отель не выбран
                                    </div>
                                    : <a href={props.businessTrip.hotel.link} target="_blank" rel="noreferrer">
                                        <div>
                                            Информация:
                                            <div className={classes.description}>
                                                Отель: {props.businessTrip.hotel.name}
                                            </div>
                                            <div className={classes.description}>
                                                Заселение: {props.businessTrip.hotel.checkIn}
                                            </div>
                                            <div className={classes.description}>
                                                Выселение: {props.businessTrip.hotel.checkOut}
                                            </div>
                                        </div>
                                    </a>
                            }
                            {
                                props.businessTrip?.hotel?.name === undefined
                                    ? <NavLink to={`/business-trips/${id}/hotel`}>
                                        Выбрать...
                                    </NavLink>
                                    : <NavLink to={`/business-trips/${id}/hotel`}>
                                        Изменить...
                                    </NavLink>
                            }
                            <div className={classes.footer}>
                                {
                                    props.businessTrip?.hotel?.price === undefined
                                        ? "Общий расход: 0 руб"
                                        : "Общий расход: " + props.businessTrip.hotel.price + " руб"
                                }
                            </div>
                        </div>
                        <div className={classes.board_container}>
                            <div className={classes.header}>
                                Расходы
                            </div>
                            <NavLink to={`/business-trips/${id}/expenses`} className={classes.footer}>
                                Посмотреть
                            </NavLink>
                        </div>
                        <div className={classes.board_container}>
                            <div className={classes.header}>
                                Отчёт
                            </div>
                            <a href='http://127.0.0.1:8000/account/some/' className={classes.footer}>
                                Сформировать отчёт
                            </a>
                        </div>
                    </div>
                    : null
            }
        </div>
    );
};

const mapStateToProps = (state) => {
    return {
        initialized: state.businessTripsData.initialized,
        businessTrips: state.businessTripsData.businessTrips,
        businessTrip: state.businessTripsData.businessTrip,
        userId: state.auth.id,
    }
};

export default compose(connect(mapStateToProps,
        {initializeBTInfo, postBusinessTripsTC, putBusinessTripsTC, setBusinessTripInfoTC}),
    withRouter)(BusinessTripInfo);
