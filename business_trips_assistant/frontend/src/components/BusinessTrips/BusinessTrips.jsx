import classes from "./BusinessTrips.module.css";
import {compose} from "redux";
import {connect} from "react-redux";
import {addBusinessTrip, removeBusinessTrip} from "../../redux/businessTripsReducer";
import BusinessTripConstructor from "./BusinessTripConstructor/BusinessTripConstructor";
import {NavLink} from "react-router-dom";
import {useState} from "react";

const BusinessTrips = (props) => {
    const onDelete = (id) => {
        props.removeBusinessTrip(id);
        setBusinessTrips(props.businessTrips.filter(bt => (bt.status === status || status === "Все") && bt.id !== id));
    }

    const onFilter = () => {
        setBusinessTrips(props.businessTrips.filter(bt => (bt.status === status || status === "Все")));
    }


    const changeFilter = () => {
        switch (status) {
            case "Все":
                setStatus("Активная");
                return;
            case "Активная":
                setStatus("Запланированная");
                return;
            case "Запланированная":
                setStatus("Завершённая");
                return;
            case "Завершённая":
                setStatus("Все");
                return;
            default:
                setStatus("Все");
                return;
        }
    }

    const [status, setStatus] = useState("Все");
    const [businessTrips, setBusinessTrips] = useState(props.businessTrips);

    return (
        <div className={classes.body_container}>
            <div className={classes.new_bt}>
                <div>
                    Новая командировка
                </div>
                <NavLink to={`/business-trips/${props.countBusinessTrips}`} className={classes.button}>
                    Создать
                </NavLink>
            </div>
            <div className={classes.filter}>
                <div onClick={changeFilter}>
                    Статус: {status}
                </div>
                <button className={classes.button} onClick={onFilter}>
                    Фильтровать
                </button>
            </div>
            <div>
                {
                    businessTrips.map((businessTrip) =>
                        <BusinessTripConstructor businessTrip={businessTrip}
                                                 onDelete={onDelete}/>)
                }
            </div>
        </div>
    );
}

const mapStateToProps = (state) => {
    return {
        countBusinessTrips: state.businessTripsData.nextId,
        businessTrips: state.businessTripsData.businessTrips,
    }
};

export default compose(connect(mapStateToProps, {addBusinessTrip, removeBusinessTrip}))(BusinessTrips);
