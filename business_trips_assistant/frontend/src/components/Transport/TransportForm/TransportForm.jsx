import classes from "./TransportForm.module.css";
import {NavLink} from "react-router-dom";
import {Formik, Form} from 'formik';
import cn from "classnames";
import TextInput from "../../Common/TextInput";
import CheckBox from "../../Common/CheckBox";
import {useState} from "react";
import SmartTextInput from "../../Common/SmartTextInput";

const validate = (values) => {
    const errors = {};

    if (!values.name) {
        errors.name = 'Обязательно';
    } else if (values.name.length > 30) {
        errors.name = 'Должно быть 30 символов или меньше';
    }

    if (!values.begin) {
        errors.begin = 'Обязательно';
    }

    if (!values.end) {
        errors.end = 'Обязательно';
    }

    return errors;
};

const TransportForm = (props) => {
    const businessTrip = props.businessTrips.find((bt) => bt.id === props.id) || {
        id: props.id,
        name: '',
        fromCity: '',
        toCity: '',
        fromStation: '',
        toStation: '',
        begin: '',
        end: '',
        budget: '',
        transport: [""],
        hotel: "Неизвестно",
        //dateFrom: "Неизвестно", //todo: refactor name
        //dateTo: "Неизвестно", //todo: refactor name
        status: "Запланирована",
    }
    const [checkboxTo, setCheckboxTo] = useState(false);
    const [checkboxFrom, setCheckboxFrom] = useState(false);
    return (
        <Formik
            initialValues={businessTrip}
            validate={validate}

            onSubmit={(values) => {
                const bt = {
                    user_id: 2,
                    id: values.id,
                    name: values.name,
                    fromCity: values.fromCity,
                    toCity: values.toCity,
                    begin: values.begin,
                    end: values.end,
                    budget: values.budget,
                    transport: values.transport,
                    hotel: values.hotel,
                    //dateFrom: values.dateFrom, //todo: refactor name
                    //dateTo: values.dateTo, //todo: refactor name
                    status: values.status,
                }

                if (props.id === props.countBusinessTrips) {
                    props.postBusinessTripsTC(bt);
                } else
                    props.editBusinessTrip(props.id, bt);
            }}>
            <Form className={classes.body_container}>
                <div className={classes.first_row}>
                    <div>
                        Транспорт
                    </div>
                    <NavLink to={`/business-trips/${props.id}`} className={cn(classes.button, classes.exit)}>
                        &#8592; {/*todo: exit icon*/}
                    </NavLink>
                </div>
                <div className={classes.row}>
                    <TextInput
                        name="fromCity"
                        type="text"
                        placeholder="Откуда..."
                        label="Откуда"
                        disabled={true}
                    />
                    <TextInput
                        name="toCity"
                        type="text"
                        placeholder="Куда..."
                        label="Куда"
                        disabled={true}
                    />
                </div>
                <div className={classes.row}>
                    <SmartTextInput
                        name="fromStation"
                        type="text"
                        placeholder="Станция/Аэропорт..."
                        disabled={checkboxFrom}
                    />
                    <SmartTextInput
                        name="toStation"
                        type="text"
                        placeholder="Станция/Аэропорт..."
                        disabled={checkboxTo}
                    />
                </div>
                <div className={classes.checkbox_row}>
                    <CheckBox
                        name="fromAnyStation"
                        type="checkbox"
                        label="Любая станция/аэропорт"
                        onClick={() => setCheckboxFrom(!checkboxFrom)}
                    />
                    <CheckBox
                        name="toAnyStation"
                        type="checkbox"
                        label="Любая станция/аэропорт"
                        onClick={() => setCheckboxTo(!checkboxTo)}
                    />
                </div>
                <div className={classes.last_row}>
                    <TextInput
                        name="type"
                        type="text"
                        placeholder="Вид транспорта..."
                        label="Вид транспорта"
                    />
                    <div className={classes.third_row_second_group}>
                        <TextInput
                            name="end"
                            type="date"
                            label="Отправление"
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

export default TransportForm;
