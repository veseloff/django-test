import classes from "./TextInput.module.css";
import Select from "react-select";

const SelectInput = ({label, ...props}) => {
    return (
        <>
            <div className={classes.input_text_wrapper}>
                <label className={classes.label}>{label}</label>
                <Select
                    styles={{
                        option: (provided) => ({
                            ...provided,
                            '&:last-of-type': {
                                borderBottomLeftRadius: 15,
                                borderBottomRightRadius: 15,
                                marginBottom: -4,
                            }
                        }),
                        menu: (provided) => ({
                            ...provided,
                            marginTop: -18,
                            paddingTop: 15,
                            borderBottomLeftRadius: 15,
                            borderTopLeftRadius: 0,
                            borderTopRightRadius: 0,
                            borderBottomRightRadius: 15,
                        }),
                        input: (provided) => ({
                            ...provided,
                            marginTop: 0,
                            height: 16,
                            paddingTop: 1,
                            paddingBottom: 1,
                            boxSizing: 'border-box',
                            color: '#000000',
                            fontSize: 13,
                            fontFamily: 'Arial',
                        }),
                        control: (provided) => ({
                            ...provided,
                            borderRadius: 15,
                            minHeight: 0,
                            height: 30,
                            zIndex: 2,
                        }),
                        singleValue: (provided) => ({
                            ...provided,
                            color: '#000000',
                            fontSize: 13,
                            height: 16,
                            fontFamily: 'Arial',
                        }),
                        placeholder: (provided) => ({
                            ...provided,
                            color: '#C4C4C4',
                            fontSize: 13,
                            fontFamily: 'Arial',
                        }),
                        valueContainer: (provided) => ({
                            ...provided,
                            height: 26,
                            paddingTop: 1,
                            paddingBottom: 1,
                            boxSizing: 'border-box',
                            marginTop: -1,
                        }),
                        indicatorsContainer: (provided) => ({
                            ...provided,
                            height: 30,
                        }),
                    }}
                    {...props}>
                </Select>
            </div>
        </>
    );
};

export default SelectInput;