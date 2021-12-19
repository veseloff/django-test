import classes from "./BusinessTrips.module.css";
import {compose} from "redux";
import {connect} from "react-redux";
import {deleteBusinessTripsTC, setBusinessTripsTC, uninitializedSuccess} from "../../redux/businessTripsReducer";
import BusinessTripConstructor from "./BusinessTripConstructor/BusinessTripConstructor";
import {NavLink} from "react-router-dom";
import {useEffect, useState} from "react";

const BusinessTrips = (props) => {
    const [status, setStatus] = useState("Все");

    useEffect(() => {
            props.setBusinessTripsTC(props.userId);
            props.uninitializedSuccess();
        },
        // eslint-disable-next-line
        []);

    const onDelete = (id) => {
        props.deleteBusinessTripsTC(props.userId, id);
    }

    const changeFilter = () => {
        switch (status) {
            case "Все":
                setStatus("Действующая");
                return;
            case "Действующая":
                setStatus("Закончена");
                return;
            case "Закончена":
                setStatus("Будущая");
                return;
            case "Будущая":
                setStatus("Все");
                return;
            default:
                setStatus("Все");
                return;
        }
    }

    return (
        <div className={classes.body_container}>
            <div className={classes.new_bt}>
                <div>
                    Новая командировка
                </div>
                <NavLink to={`/business-trips/new`} className={classes.button}>
                    Создать
                </NavLink>
            </div>
            <div className={classes.filter}>
                <div onClick={changeFilter}>
                    Статус: {status}
                </div>
            </div>
            <div>
                {
                    props.businessTrips !== undefined
                        ? props.businessTrips
                            .filter(bt => (bt.status === status || status === "Все"))
                            .map((businessTrip, index) =>
                                <BusinessTripConstructor businessTrip={businessTrip}
                                                         onDelete={onDelete} key={index}/>)
                        : null
                }
            </div>
        </div>
    );
}

const mapStateToProps = (state) => {
    return {
        businessTrips: state.businessTripsData.businessTrips,
        userId: state.auth.id,
    }
};

export default compose(connect(mapStateToProps, {
    setBusinessTripsTC,
    deleteBusinessTripsTC,
    uninitializedSuccess,
}))(BusinessTrips);
