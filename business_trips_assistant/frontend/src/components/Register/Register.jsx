import {compose} from "redux";
import {connect} from "react-redux";
import {getAuthMeTC, postAuthLoginTC, postAuthRegisterTC, postTelegramTC} from "../../redux/authReducer";
import classes from "./Register.module.css";
import RegisterForm from "./RegisterForm";
import AuthRedirect from "../../Hoc/AuthRedirect";
import cn from "classnames";
import {NavLink} from "react-router-dom";

const Register = (props) => {
    return (
        <div className={classes.container}>
            <div className={classes.pseudo}/>
            <div className={classes.container_login}>
                <div className={classes.content}>
                    <div className={classes.head}>
                        <div/>
                        <h1>Sign Up</h1>
                        <div className={classes.exit_button}>
                            <NavLink to={`/login`} className={cn(classes.button, classes.exit)}>
                                &#8592; {/*todo: exit icon*/}
                            </NavLink>
                        </div>
                    </div>
                    <RegisterForm {...props}/>
                </div>
            </div>
            <div className={classes.pseudo}/>
        </div>
    );
}

let mapStateToProps = (state) => {
    return {
        isAuth: state.auth.isAuth,
        email: state.auth.email,
        username: state.auth.username,
        userId: state.auth.id,
    }
}

export default compose(connect(mapStateToProps, {
    postAuthRegisterTC,
    getAuthMeTC,
    postAuthLoginTC,
    postTelegramTC,
}), AuthRedirect)(Register);