import classes from "./Header.module.css";
import logo from "./../../assets/logo.png";
import {compose} from "redux";
import {connect} from "react-redux";
import withLoginRedirect from "../../Hoc/LoginRedirect";
import {deleteAuthLoginTC} from "../../redux/authReducer";

const Header = (props) => {
    return (
        <header className={classes.header_container}>
            <div className={classes.logo_container}>
                <img src={logo} alt="logo"/>
            </div>
            <div className={classes.profile_name_container} onClick={() => {props.deleteAuthLoginTC()}}>
                <div>
                    {props.username}
                </div>
                <div className={classes.avatar}/>
            </div>
        </header>
    );
}

const mapStateToProps = (state) => {
    return {
        username: state.auth.username,
    }
};

export default compose(connect(mapStateToProps, {deleteAuthLoginTC}), withLoginRedirect)(Header);
