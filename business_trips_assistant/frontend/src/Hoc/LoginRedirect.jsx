import {Redirect} from "react-router-dom";
import React from "react";
import {connect} from "react-redux";

const withLoginRedirect = (Component) => {
    class RedirectComponent extends React.Component {
        render() {
            return !this.props.isAuth ? <Redirect to={"/login"}/> : <Component {...this.props}/>;
        }
    }

    return connect((state) => ({isAuth: state.auth.isAuth}))(RedirectComponent);
}

export default withLoginRedirect;