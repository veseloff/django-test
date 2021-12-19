import classes from "./App.module.css";
import {connect, Provider} from "react-redux";
import {BrowserRouter, Redirect, Route, Switch} from "react-router-dom";
import Header from "./components/Header/Header";
import BusinessTrips from "./components/BusinessTrips/BusinessTrips";
import BusinessTripInfo from "./components/BusinessTripInfo/BusinessTripInfo";
import Transport from "./components/Transport/Transport";
import Hotel from "./components/Hotel/Hotel";
import Expenses from "./components/Expenses/Expenses";
import store from "./redux/reduxStore";
import cn from "classnames";
import {initializeApp} from "./redux/appReducer";
import Login from "./components/Login/Login";
import {useEffect} from "react";
import Register from "./components/Register/Register";

const App = (props) => {
    useEffect(() => {
        props.initializeApp()
    }, []);

    if (!props.initialized)
        return null
    return (
        <Switch>
            <Route path={"/login"} render={() => <Login/>}/>
            <Route path={"/register"} render={() => <Register/>}/>
            <Route exact path={"/"}>
                <Redirect to={"/login"}/>
            </Route>
            <Route path={"/"}>
                <div className={classes.app_wrapper}>
                    <div className={cn(classes.app_content_wrapper, classes.header_wrapper)}>
                        <Header/>
                    </div>
                    <div className={cn(classes.app_content_wrapper, classes.app_body_wrapper)}>
                        <Switch>
                            <Route exact path={"/business-trips"} render={() => <BusinessTrips/>}/>
                            <Route exact path={"/business-trips/:businessTripId?"}
                                   render={() => <BusinessTripInfo/>}/>
                            <Route exact path={"/business-trips/:businessTripId?/transport/:direction?"}
                                   render={() => <Transport/>}/>
                            <Route exact path={"/business-trips/:businessTripId?/hotel"} render={() => <Hotel/>}/>
                            <Route exact path={"/business-trips/:businessTripId?/expenses"}
                                   render={() => <Expenses/>}/>
                        </Switch>
                    </div>
                </div>
            </Route>
        </Switch>
    );
}

const mapStateToProps = (state) => {
    return {
        initialized: state.app.initialized,
    }
}

const AppContainer = connect(mapStateToProps,
    {
        initializeApp
    }
)(App);

const ReactApp = () => {
    return (
        <BrowserRouter>
            <Provider store={store}>
                <AppContainer/>
            </Provider>
        </BrowserRouter>
    )
}

export default ReactApp;
