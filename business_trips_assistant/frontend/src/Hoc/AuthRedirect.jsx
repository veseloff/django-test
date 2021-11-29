import {Redirect} from "react-router-dom";
import React from "react";
import {connect} from "react-redux";

const withAuthRedirect = (Component) => {
    class RedirectComponent extends React.Component {
        render() {
            return this.props.isAuth ? <Redirect to={`/business-trips`}/> : <Component {...this.props}/>;
        }
    }

    return connect((state) => ({isAuth: state.auth.isAuth})) (RedirectComponent);
}

export default withAuthRedirect;