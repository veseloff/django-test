import classes from "./Hotel.module.css";
import HotelForm from "./HotelForm/HotelForm";
import {compose} from "redux";
import {connect} from "react-redux";
import {withRouter} from "react-router-dom";
import HotelConstructor from "./HotelConstructor/HotelConstructor";
import {setHotelsTC} from "../../redux/hotelReducer";
import Paginator from "../Common/Paginator/Paginator";
import {useEffect, useState} from "react";

const Hotel = (props) => {
    const id = isNaN(Number(props.match.params.businessTripId))
        ? (props.businessTrip.id || 'new')
        : Number(props.match.params.businessTripId);

    const [currentPage, setCurrentPage] = useState(1);
    const pageSize = 25;

    useEffect(() => {
        const info = {...props.hotelsDataSearch};
        info.offset = (currentPage - 1) * 25;
        props.setHotelsTC(info);
        }, [currentPage]
    );

    return (
        <div className={classes.body_container}>
            <HotelForm {...props} id={id} currentPage={currentPage}/>
            <div className={classes.body_wrapper}>
                {
                    props.hotels !== undefined
                        ? props.hotels
                            .map((hotel) =>
                                <HotelConstructor {...hotel}/>)
                        : null
                }
                <Paginator count={props.count} pageSize={pageSize} currentPage={currentPage}
                           setCurrentPage={setCurrentPage}/>
            </div>
        </div>
    );
}

const mapStateToProps = (state) => {
    return {
        hotels: state.hotelsData.hotels,
        hotelsDataSearch: state.hotelsData.hotelsDataSearch,
        count: state.hotelsData.count,
        businessTrip: state.businessTripsData.businessTrip,
    }
};

export default compose(connect(mapStateToProps,
    {setHotelsTC}), withRouter)(Hotel);
