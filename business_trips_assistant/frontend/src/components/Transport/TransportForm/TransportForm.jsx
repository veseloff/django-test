import classes from "./TransportForm.module.css";
import {NavLink} from "react-router-dom";
import {Formik, Form} from 'formik';
import cn from "classnames";
import TextInput from "../../Common/FormControl/TextInput";
import {useState} from "react";
import SelectInput from "../../Common/FormControl/SelectInput";

const validate = (values) => {
    const errors = {};

    if (!values.date) {
        errors.date = 'Обязательно';
    }

    return errors;
};

const TransportForm = (props) => {
    const initialData = {
        toCity: props.direction === 'there' ? props.businessTrip.toCity : props.businessTrip.fromCity,
        fromCity: props.direction === 'there' ? props.businessTrip.fromCity : props.businessTrip.toCity,
        toStation: '',
        fromStation: '',
        type: '',
        date: '',
        fromAnyStation: false,
        toAnyStation: false,
    }

    const options = [
        {value: 1, label: 'РЖД'},
        {value: 0, label: 'Aviasales'}
    ]

    const [selectedOption, setSelectedOption] = useState(options[0]);

    const stationsFrom = props.stationsFrom?.map((station) => {
            return {
                label: station.station,
                value: station.station,
                code: station.code,
            }
        })

    const [selectedStationFrom, setSelectedStationFrom] = useState('');

    const stationsTo = props.stationsTo?.map((station) => {
            return {
                label: station.station,
                value: station.station,
                code: station.code,
            }
        })

    const [selectedStationTo, setSelectedStationTo] = useState('');

    return (
        <Formik
            initialValues={initialData}
            validate={validate}

            onSubmit={(values) => {
                const info = {
                    cityT: values.toCity,
                    cityF: values.fromCity,
                    stationT: selectedStationTo?.value,
                    stationF: selectedStationFrom?.value,
                    codeST: selectedStationTo?.code,
                    codeSF: selectedStationFrom?.code,
                    date: values.date,
                    type: selectedOption?.value,
                }
                props.setRZDTC(info);
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
                    <SelectInput
                        name="fromStation"
                        type="text"
                        label="Станция/Аэропорт"
                        placeholder="Станция/Аэропорт..."
                        options={props.direction === 'there' ? stationsFrom : stationsTo}
                        classNamePrefix="select"
                        defaultValue={selectedStationFrom}
                        onChange={setSelectedStationFrom}
                        isClearable={true}
                        zind={5}
                    />
                    <SelectInput
                        name="toStation"
                        type="text"
                        label="Станция/Аэропорт"
                        placeholder="Станция/Аэропорт..."
                        options={props.direction === 'there' ? stationsTo : stationsFrom}
                        classNamePrefix="select"
                        defaultValue={selectedStationTo}
                        onChange={setSelectedStationTo}
                        isClearable={true}
                    />
                </div>
                <div className={classes.row}>
                    <SelectInput
                        options={options}
                        classNamePrefix="select"
                        defaultValue={selectedOption}
                        onChange={setSelectedOption}
                        name="type"
                        type="text"
                        placeholder="Вид транспорта..."
                        label="Вид транспорта"
                    />
                    <div className={classes.third_row_second_group}>
                        <TextInput
                            name="date"
                            type="date"
                            label="Отправление"
                        />
                        <button type="submit" className={cn(classes.button, classes.save)}>
                            Поиск
                        </button>
                    </div>
                </div>
            </Form>
        </Formik>
    );
};

export default TransportForm;
