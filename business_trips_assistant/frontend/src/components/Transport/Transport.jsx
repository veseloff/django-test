import classes from "./Transport.module.css";
import TransportForm from "./TransportForm/TransportForm";
import {compose} from "redux";
import {connect} from "react-redux";
import {postBusinessTripsTC, setCsrfTC} from "../../redux/businessTripsReducer";
import {withRouter} from "react-router-dom";
import TransportConstructor from "./TransportConstructor/TransportConstructor";

const Transport = (props) => {
    const id = isNaN(Number(props.match.params.businessTripId))
        ? (props.businessTrip.id || 'new')
        : Number(props.match.params.businessTripId);
    return (
        <div className={classes.body_container}>
            <TransportForm {...props} id={id}/>
            <div className={classes.body_wrapper}>
                {
                    props.businessTrips !== undefined
                        ? props.businessTrips
                            .map((businessTrip, index) =>
                                <TransportConstructor businessTrip={businessTrip} key={index}/>)
                        : null
                }
            </div>
        </div>
    );
}

const mapStateToProps = (state) => {
    return {
        businessTrips: state.businessTripsData.businessTrips,
    }
};

export default compose(connect(mapStateToProps,
    {postBusinessTripsTC, setCsrfTC}), withRouter)(Transport);
