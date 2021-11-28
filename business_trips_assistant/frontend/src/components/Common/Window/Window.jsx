import cn from "classnames";
import classes from "./Window.module.css";

const Window = (props) => {
    return (
        <div className={cn(classes.wrapper, {
            [classes.hidden]: !props.visibility,
            [classes.visible]: props.visibility,
        })}>
            <div className={classes.container}>
                <div>{props.label}</div>
                <div className={classes.button_wrapper}>
                    <button className={classes.button} onClick={() => {
                        props.action(props.item);
                        props.setVisibility(false)
                    }}>
                        {props.agree}
                    </button>
                    <button className={classes.button} onClick={() => {
                        props.setVisibility(false)
                    }}>
                        {props.disagree}
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Window;