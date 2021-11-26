import {useField} from "formik";
import classes from "./CheckBox.module.css";
import cn from "classnames";

const CheckBox = ({label, ...props}) => {
    const [field, meta] = useField(props);

    return (
        <>
            <div className={classes.input_text_wrapper}>
                <input className={cn(classes.input_text)} {...field} {...props}/>
                <label className={classes.label}>{label}</label>
            </div>
        </>
    );
};

export default CheckBox;