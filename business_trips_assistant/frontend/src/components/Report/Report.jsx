import classes from "./Report.module.css";
import logo from "./../../assets/logo.png";

function Report() {
    return (
        <header className={classes.header}>
            <div className={classes.header_container}>
                <img src={logo}/>
                <div className={classes.profile_name_container}>
                    <div>
                        ProfileName
                    </div>
                    <div className={classes.avatar}/>
                </div>
            </div>
        </header>
    );
}

export default Report;
