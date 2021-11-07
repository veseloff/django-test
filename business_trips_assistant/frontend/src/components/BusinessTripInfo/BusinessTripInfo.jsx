import {NavLink, withRouter} from "react-router-dom";
import classes from "./BusinessTripInfo.module.css";
import {compose} from "redux";
import {connect} from "react-redux";
import {addBusinessTrip, editBusinessTrip} from "../../redux/businessTripsReducer";
import BusinessTripInfoForm from "./BusinessTripInfoForm/BusinessTripInfoForm";

const BusinessTripInfo = (props) => {
    const id = Number(props.match.params.businessTripId || props.countBusinessTrips);

    return (
        <div className={classes.body_container}>
            <BusinessTripInfoForm {...props} id={id}/>
            <div className={classes.body_wrapper}>
                <div className={classes.board_container}>
                    <div className={classes.header}>
                        Транспорт
                    </div>
                    <NavLink to={`/business-trips/${id}/transport`}>
                        Туда:
                        <div className={classes.description}>
                            <div>Поезд 025А</div>
                            <div>Санкт-Петербург - Москва</div>
                            <div>30.09.2021 - 1.10.2021</div>
                        </div>
                    </NavLink>
                    <NavLink to={`/business-trips/${id}/transport`}>
                        Обратно:
                        <div className={classes.description}>
                            <div>Самолёт SU 38</div>
                            <div>Москва - Санкт-Петербург</div>
                            <div>10.10.2021 - 10.10.2021</div>
                        </div>
                    </NavLink>
                    <div className={classes.footer}>
                        Общий расход: 10000
                    </div>
                </div>
                <div className={classes.board_container}>
                    <div className={classes.header}>
                        Отель
                    </div>
                    <NavLink to={`/business-trips/${id}/hotel`}>
                        КОСМОС
                    </NavLink>
                    <NavLink to={`/business-trips/${id}/hotel`}>
                        Ленинградский
                    </NavLink>
                    <NavLink to={`/business-trips/${id}/hotel`} className={classes.footer}>
                        Centeral
                    </NavLink>
                </div>
                <div className={classes.board_container}>
                    <div className={classes.header}>
                        Расходы
                    </div>
                    <div className={classes.footer}>
                        Посмотреть
                    </div>
                </div>
                <div className={classes.board_container}>
                    <div className={classes.header}>
                        Отчёт
                    </div>
                    <div className={classes.footer}>
                        Сформировать отчёт
                    </div>
                </div>
            </div>
        </div>
    );
};

const mapStateToProps = (state) => {
    return {
        countBusinessTrips: state.businessTripsData.nextId,
        businessTrips: state.businessTripsData.businessTrips,
    }
};

export default compose(connect(mapStateToProps, {addBusinessTrip, editBusinessTrip}), withRouter)(BusinessTripInfo);
