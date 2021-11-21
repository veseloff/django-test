import {useField} from "formik";
import classes from "./TextInput.module.css";
import cn from "classnames";

const SmartTextInput = ({label, ...props}) => {
    const [field, meta] = useField(props);
    props.value = props.disabled ? "" : props.value;
    return (
        <>
            <div className={classes.input_text_wrapper}>
                <label className={classes.label}>{label}</label>
                <input className={cn(classes.input_text, {
                    [classes.error]: meta.touched && meta.error
                })} {...field} {...props}/>
                {meta.touched && meta.error ? (
                    <div className={classes.error_wrapper}>
                        <div className={classes.error_container}>
                            {meta.error}
                        </div>
                    </div>
                ) : null}
            </div>
        </>
    );
};

export default SmartTextInput;