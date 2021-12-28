import classes from "./HotelForm.module.css";
import {NavLink} from "react-router-dom";
import {Formik, Form} from 'formik';
import cn from "classnames";
import TextInput from "../../Common/FormControl/TextInput";
import SelectInput from "../../Common/FormControl/SelectInput";
import {useState} from "react";
import SmartTextInput from "../../Common/FormControl/SmartTextInput";
import CheckBox from "../../Common/FormControl/CheckBox";

const validate = (values) => {
    const errors = {};

    if (!values.city) {
        errors.city = 'Обязательно';
    } else if (values.city.length > 30) {
        errors.city = 'Должно быть 30 символов или меньше';
    }

    if (!values.checkIn) {
        errors.checkIn = 'Обязательно';
    }

    if (!values.checkOut) {
        errors.checkOut = 'Обязательно';
    }

    return errors;
};

const HotelForm = (props) => {
    const initialData = {
        city: props.businessTrip.toCity,
        checkIn: '',
        checkOut: '',
        offset: props.currentPage,
        option: '',
        star: '',
        parking: '',
        wifi: '',
    }

    const options = [
        {value: 'booking', label: 'Booking'},
        {value: 'airbnb', label: 'Airbnb'}
    ]

    const [selectedOption, setSelectedOption] = useState(options[0]);
    const [parking, setParking] = useState(false);
    const [wifi, setWifi] = useState(false);

    return (
        <Formik
            initialValues={initialData}
            validate={validate}

            onSubmit={(values) => {
                const conveniences = [];
                if (parking)
                    conveniences.push("hotelfacility%3D2");
                if (wifi)
                    conveniences.push("hotelfacility%3D107");
                const data = {
                    city: values.city,
                    checkIn: values.checkIn,
                    checkOut: values.checkOut,
                    offset: values.offset,
                    option: selectedOption.value,
                    star: values.star,
                    conveniences: conveniences,
                }
                props.setHotelsTC(data);
            }}>
            <Form className={classes.body_container}>
                <div className={classes.first_row}>
                    <div>
                        Отель
                    </div>
                    <NavLink to={`/business-trips/${props.id}`} className={cn(classes.button, classes.exit)}>
                        &#8592; {/*todo: exit icon*/}
                    </NavLink>
                </div>
                <div className={classes.second_row}>
                    <TextInput
                        name="city"
                        type="text"
                        placeholder="Выберите город..."
                        label="Город"
                    />
                    <SelectInput
                        label="Выбор поисковика"
                        placeholder="Обязательно"
                        name="option"
                        type="text"
                        options={options}
                        classNamePrefix="select"
                        defaultValue={selectedOption}
                        onChange={setSelectedOption}
                    />
                </div>
                <div className={classes.third_row}>
                    <div className={classes.third_row_first_group}>
                        <TextInput
                            name="checkIn"
                            type="date"
                            label="Заезд"
                        />
                        <TextInput
                            name="checkOut"
                            type="date"
                            label="Выезд"
                        />
                    </div>
                    <div className={classes.third_row_second_group}>
                        <SmartTextInput
                            name="star"
                            type="number"
                            label="Звёзды"
                            disabled={selectedOption.value === "airbnb"}
                        />
                        <div className={classes.group}>
                            <CheckBox
                                name="parking"
                                type="checkbox"
                                label="Парковка"
                                onChange={() => setParking(!parking)}
                            />
                            <CheckBox
                                name="wifi"
                                type="checkbox"
                                label="Wi-Fi"
                                onChange={() => setWifi(!wifi)}
                            />
                        </div>
                        <button type="submit" className={cn(classes.button, classes.save)}>
                            Поиск
                        </button>
                    </div>
                </div>
            </Form>
        </Formik>
    );
};

export default HotelForm;
