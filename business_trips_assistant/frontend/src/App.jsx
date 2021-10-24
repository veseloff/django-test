import classes from "./App.module.css";
import {connect, Provider} from "react-redux";
import {BrowserRouter, Redirect, Route, Switch} from "react-router-dom";
import Header from "./components/Header/Header";
import BusinessTrips from "./components/BusinessTrips/BusinessTrips";
import BusinessTripInfo from "./components/BusinessTripInfo/BusinessTripInfo";
import Transport from "./components/Transport/Transport";
import Hotel from "./components/Hotel/Hotel";
import Expenses from "./components/Expenses/Expenses";
import Report from "./components/Report/Report";
import store from "./redux/reduxStore";
import cn from "classnames";

const App = () => {
    return (
        <BrowserRouter>
            <Provider store={store}>
                <Switch>
                    <Route path={"/login"}/>
                    <Route exact path={"/"}>
                        <Redirect to={"/business-trips"}/>
                    </Route>
                    <Route path={"/"}>
                        <div className={classes.app_wrapper}>
                            <div className={cn(classes.app_content_wrapper, classes.header_wrapper)}>
                                <Header/>
                            </div>
                            <div className={cn(classes.app_content_wrapper, classes.body_wrapper)}>
                                <Switch>
                                    <Route exact path={"/business-trips"} render={() => <BusinessTrips/>}/>
                                    <Route exact path={"/business-trips/:businessTripId?"}
                                           render={() => <BusinessTripInfo/>}/>
                                    <Route exact path={"/business-trips/:businessTripId?/transport"}
                                           render={() => <Transport/>}/>
                                    <Route exact path={"/business-trips/:businessTripId?/hotel"} render={() => <Hotel/>}/>
                                    <Route exact path={"/business-trips/:businessTripId?/expenses"}
                                           render={() => <Expenses/>}/>
                                    <Route path={"/business-trips/:businessTripId?/report"} render={() => <Report/>}/>

                                    {/*<Route path={"/"}>
                                    <Redirect to={"/404"}/>
                                </Route>*/}
                                </Switch>
                                {/*<Navigation id={this.props.id}/>
                        <div className={classes.content}>
                            <Suspense fallback={<Preloader/>}>
                                <Switch>
                                    <Route path={"/profile/:userId?"} render={() => <Profile/>}/>
                                    <Route exact path={"/profile"}>
                                        <Redirect to={"/login"}/>
                                    </Route>
                                    <Route path={"/profile/null"}>
                                        <Redirect to={"/login"}/>
                                    </Route>
                                    <Route path={"/messages"} render={() => <Messages/>}/>
                                    <Route exact path={"/users"} render={() => <UsersContainer/>}/>
                                    <Route path={"/404"} render={() => <NotFound/>}/>
                                    <Route path={"/music/"} render={() => <Music/>}/>

                                    <Route path={"/"}>
                                        <Redirect to={"/404"}/>
                                    </Route>
                                </Switch>
                            </Suspense>
                        </div>*/}
                            </div>
                        </div>
                    </Route>
                </Switch>
            </Provider>
        </BrowserRouter>
    );
}

export default App;
