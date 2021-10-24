import classes from "./Header.module.css";
import logo from "./../../assets/logo.png";

const Header = () => {
    return (
        <header className={classes.header_container}>
            <div className={classes.logo_container}>
                <img src={logo}/>
            </div>
            <div className={classes.profile_name_container}>
                <div>
                    ProfileName
                </div>
                <div className={classes.avatar}/>
            </div>
        </header>
    );
}

export default Header;
