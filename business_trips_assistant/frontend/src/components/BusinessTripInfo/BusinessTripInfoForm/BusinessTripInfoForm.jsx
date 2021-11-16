import classes from "./BusinessTripInfoForm.module.css";
import {NavLink} from "react-router-dom";
import {Formik, Form} from 'formik';
import cn from "classnames";
import TextInput from "../../Common/TextInput";
import Cookies from 'js-cookie';

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

const BusinessTripInfoForm = (props) => {
    const businessTrip = props.businessTrips.find((bt) => bt.id === props.id) || {
        id: props.id,
        name: '',
        fromCity: '',
        toCity: '',
        begin: '',
        end: '',
        budget: '',
        transport: [""],
        hotel: "Неизвестно",
        //dateFrom: "Неизвестно", //todo: refactor name
        //dateTo: "Неизвестно", //todo: refactor name
        status: "Запланирована",
    }

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
                    /*props.setCsrfTC();
                    console.log("1")
                    console.log(Cookies.get('csrftoken'))*/
                    props.postBusinessTripsTC(bt);
                }
                else
                    props.editBusinessTrip(props.id, bt);
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

export default BusinessTripInfoForm;
