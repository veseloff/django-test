import classes from "./BusinessTripInfo.module.css";
import {NavLink, withRouter} from "react-router-dom";
import {Formik, Form, useField} from 'formik';
import cn from "classnames";
import {compose} from "redux";
import {connect} from "react-redux";
import {addBusinessTrip, editBusinessTrip} from "../../redux/businessTripsReducer";
import TextInput from "../Common/TextInput";

const validate = (values) => {
    const errors = {};

    if (!values.name) {
        errors.name = 'Обязательно';
    } else if (values.name.length > 30) {
        errors.name = 'Должно быть 30 символов или меньше';
    }

    if (!values.fromCity) {
        errors.fromCity = 'Обязательно';
    } else if (values.fromCity.length > 20) {
        errors.fromCity = 'Должно быть 20 символов или меньше';
    }

    if (!values.toCity) {
        errors.toCity = 'Обязательно';
    } else if (values.toCity.length > 20) {
        errors.toCity = 'Должно быть 20 символов или меньше';
    }

    if (!values.begin) {
        errors.begin = 'Обязательно';
    }

    if (!values.end) {
        errors.end = 'Обязательно';
    }

    return errors;
};

const BusinessTripInfo = (props) => {
    const id = Number(props.match.params.businessTripId || props.countBusinessTrips);
    const businessTrip = props.businessTrips.find((bt) => bt.id === id) || {
        id: id,
        name: '',
        fromCity: '',
        toCity: '',
        begin: '',
        end: '',
        budget: '',
        transport: [""],
        hotel: "Неизвестно",
        dateFrom: "Неизвестно", //todo: refactor name
        dateTo: "Неизвестно", //todo: refactor name
        status: "Запланирована",
    }

    return (
        <Formik
            initialValues={businessTrip}
            validate={validate}

            onSubmit={(values) => {
                const bt = {
                    id: values.id,
                    name: values.name,
                    fromCity: values.fromCity,
                    toCity: values.toCity,
                    begin: values.begin,
                    end: values.end,
                    budget: values.budget,
                    transport: values.transport,
                    hotel: values.hotel,
                    dateFrom: values.dateFrom, //todo: refactor name
                    dateTo: values.dateTo, //todo: refactor name
                    status: values.status,
                }

                if (id === props.countBusinessTrips)
                    props.addBusinessTrip(bt);
                else
                    props.editBusinessTrip(id, bt);
            }}>
            <Form className={classes.body_container}>
                <div className={classes.first_row}>
                    <TextInput
                        name="name"
                        type="text"
                        placeholder="Название командировки..."
                        label="Название командировки"
                    />
                    <NavLink to={`/business-trips`} className={cn(classes.button, classes.exit)}>
                        &#8592; {/*todo: exit icon*/}
                    </NavLink>
                </div>
                <div className={classes.second_row}>
                    <TextInput
                        name="fromCity"
                        type="text"
                        placeholder="Откуда..."
                        label="Откуда"
                    />
                    <TextInput
                        name="toCity"
                        type="text"
                        placeholder="Куда..."
                        label="Куда"
                    />
                </div>
                <div className={classes.third_row}>
                    <div className={classes.third_row_first_group}>
                        <TextInput
                            name="begin"
                            type="date"
                            label="Начало"
                        />
                        <TextInput
                            name="end"
                            type="date"
                            label="Конец"
                        />
                    </div>
                    <div className={classes.third_row_second_group}>
                        <TextInput
                            name="budget"
                            type="number"
                            placeholder="Бюджет..."
                            label="Бюджет"
                        />
                        <button type="submit" className={cn(classes.button, classes.save)}>
                            Сохранить
                        </button>
                    </div>
                </div>
            </Form>
        </Formik>
    );
};

const mapStateToProps = (state) => {
    return {
        countBusinessTrips: state.businessTripsData.nextId,
        businessTrips: state.businessTripsData.businessTrips,
    }
};

export default compose(connect(mapStateToProps, {addBusinessTrip, editBusinessTrip}), withRouter)(BusinessTripInfo);
