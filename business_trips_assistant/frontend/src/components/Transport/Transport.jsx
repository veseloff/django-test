import classes from "./Transport.module.css";
import logo from "./../../assets/logo.png";

function Transport() {
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

export default Transport;
