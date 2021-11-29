import {Formik, Form} from 'formik';
import classes from "./Login.module.css";
import TextInput from "../Common/FormControl/TextInput";
import {NavLink} from "react-router-dom";
import {postAuthLoginTC} from "../../redux/authReducer";

const validate = (values) => {
    const errors = {};

    if (!values.username) {
        errors.username = 'Обязательно';
    }

    if (!values.password) {
        errors.password = 'Обязательно';
    }

    return errors;
};

const LoginForm = (props) => {
    const initVal = {
        username: '',
        password: '',
    }

    return (
        <Formik
            initialValues={initVal}
            validate={validate}

            onSubmit={(values) => {
                const data = {
                    username: values.username,
                    password: values.password,
                }

                props.postAuthLoginTC(data);
            }}>
            <Form className={classes.form}>
                <div>
                    <TextInput
                        name="username"
                        type="text"
                        placeholder="Username..."
                        label="Логин"
                    />
                </div>
                <div>
                    <TextInput
                        name="password"
                        type="password"
                        placeholder="Password..."
                        label="Пароль"
                    />
                </div>
                <button type="submit" className={classes.button}>
                    Войти
                </button>
                <NavLink to={`/register`} className={classes.button}>
                    Зарегистрироваться
                </NavLink>
            </Form>
        </Formik>
    );
}

export default LoginForm;