import classes from "./BusinessTripInfoForm.module.css";
import {NavLink} from "react-router-dom";
import {Formik, Form} from 'formik';
import cn from "classnames";
import TextInput from "../../Common/FormControl/TextInput";
import {useState} from "react";
import SelectInput from "../../Common/FormControl/SelectInput";

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

    if (!values.budget) {
        errors.budget = 'Обязательно';
    }

    return errors;
};

const BusinessTripInfoForm = (props) => {
    const map = new Map();
    map.set("Закончена", 0);
    map.set("Действующая", 1);
    map.set("Будущая", 2);

    const businessTrip = props.businessTrip.name !== undefined
        ? props.businessTrip
        : {
            userId: 2,
            name: '',
            fromCity: '',
            toCity: '',
            begin: '',
            end: '',
            budget: '',
            transport: [""],
            hotel: "Неизвестно",
            status: "Будущая",
        }

    const options = [
        {value: 'Будущая', label: 'Будущая'},
        {value: 'Закончена', label: 'Закончена'},
        {value: 'Действующая', label: 'Действующая'},
    ]

    const [selectedOption, setSelectedOption] = useState(options.find(option => option.value === businessTrip.status));

    return (
        <Formik
            initialValues={businessTrip}
            validate={validate}

            onSubmit={(values) => {
                const bt = {
                    userId: 2,
                    name: values.name,
                    fromCity: values.fromCity,
                    toCity: values.toCity,
                    begin: values.begin,
                    end: values.end,
                    budget: values.budget,
                    transport: values.transport,
                    hotel: values.hotel,
                    status: map.get(selectedOption.value),
                }

                if (props.id === 'new')
                    props.postBusinessTripsTC(bt);
                else
                    props.putBusinessTripsTC(props.id, bt);
            }}>
            <Form className={classes.body_container}>
                <div className={classes.row}>
                    <TextInput
                        name="name"
                        type="text"
                        placeholder="Название командировки..."
                        label="Название командировки"
                    />
                    <div className={classes.first_row_second_group}>
                        <SelectInput
                            label="Статус"
                            placeholder="Обязательно"
                            name="option"
                            type="text"
                            options={options}
                            classNamePrefix="select"
                            defaultValue={selectedOption}
                            onChange={setSelectedOption}
                        />
                        <NavLink to={`/business-trips`} className={cn(classes.button, classes.exit)}>
                            &#8592; {/*todo: exit icon*/}
                        </NavLink>
                    </div>
                </div>
                <div className={classes.row}>
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
                <div className={classes.row}>
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
