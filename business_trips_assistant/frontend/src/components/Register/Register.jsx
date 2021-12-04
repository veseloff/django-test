import {compose} from "redux";
import {connect} from "react-redux";
import {getAuthMeTC, postAuthLoginTC, postAuthRegisterTC} from "../../redux/authReducer";
import classes from "./Register.module.css";
import RegisterForm from "./RegisterForm";
import AuthRedirect from "../../Hoc/AuthRedirect";

const Register = (props) => {
    return (
        <div className={classes.container}>
            <div className={classes.pseudo}/>
            <div className={classes.container_login}>
                <div className={classes.content}>
                    <h1>Sign Up</h1>
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

export default compose(connect(mapStateToProps, {postAuthRegisterTC, getAuthMeTC, postAuthLoginTC}), AuthRedirect)(Register);