import {compose} from "redux";
import {connect} from "react-redux";
import {postAuthLoginTC} from "../../redux/authReducer";
import classes from "./Login.module.css";
import LoginForm from "./LoginForm";
import AuthRedirect from "../../Hoc/AuthRedirect";

const Login = (props) => {
    return (
        <div className={classes.container}>
            <div className={classes.pseudo}/>
            <div className={classes.container_login}>
                <div className={classes.content}>
                    <h1>Sign In</h1>
                    <LoginForm {...props}/>
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
        userId: state.auth.userId,
    }
}

export default compose(connect(mapStateToProps, {postAuthLoginTC}), AuthRedirect)(Login);