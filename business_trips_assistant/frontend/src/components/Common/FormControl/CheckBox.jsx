import classes from "./CheckBox.module.css";
import cn from "classnames";

const CheckBox = ({label, ...props}) => {
    return (
        <>
            <div className={classes.input_text_wrapper}>
                <input className={cn(classes.input_text)} {...props}/>
                <label className={classes.label}>{label}</label>
            </div>
        </>
    );
};

export default CheckBox;