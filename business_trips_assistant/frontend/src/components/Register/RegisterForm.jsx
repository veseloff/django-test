import {Formik, Form} from 'formik';
import classes from "./Register.module.css";
import TextInput from "../Common/FormControl/TextInput";
import {NavLink} from "react-router-dom";
import {getAuthMeTC, postAuthLoginTC, postTelegramTC} from "../../redux/authReducer";

const validate = (values) => {
    const errors = {};

    if (!values.username) {
        errors.username = 'Обязательно';
    }

    if (values.username.length > 150) {
        errors.username = 'Слишком большое имя пользователя';
    }

    if (!values.password) {
        errors.password = 'Обязательно';
    }

    if (values.password.length < 8) {
        errors.password = 'Слишком короткий пароль';
    }

    if (!values.repeatPassword) {
        errors.repeatPassword = 'Обязательно';
    }

    if (values.repeatPassword.length < 8) {
        errors.repeatPassword = 'Слишком короткий пароль';
    }

    if (values.repeatPassword !== values.password) {
        errors.repeatPassword = 'Пароли должны совпадать';
    }

    if (!values.email) {
        errors.email = 'Обязательно';
    }

    if (!/(\w+)@(\D+).(\D+)/.test(values.email)) {
        errors.email = 'Неверный формат';
    }

    return errors;
};

const RegisterForm = (props) => {
    const initVal = {
        username: '',
        password: '',
        repeatPassword: '',
        email: '',
        tgId: '',
        firstname: '',
        lastname: '',
    }

    return (
        <Formik
            initialValues={initVal}
            validate={validate}

            onSubmit={(values) => {
                const data = {
                    username: values.username,
                    password: values.password,
                    email: values.email,
                    firstname: values.firstname,
                    lastname: values.lastname,
                }

                props.postAuthRegisterTC(data)
                    .then(response => {
                        if (response.status === "Success")
                            props.postAuthLoginTC({username: data.username, password: data.password})
                                .then(response => {
                                    if (response.status === "Success")
                                        props.getAuthMeTC().then(response => {
                                            props.postTelegramTC({idTelegram: values.tgId});
                                        })
                                    else
                                        alert(response);
                                })
                        else
                            alert(response.username[0]);
                    })
            }}>
            <Form className={classes.form}>
                <div>
                    <TextInput
                        name="email"
                        type="text"
                        placeholder="Email..."
                        label="Email"
                    />
                </div>
                <div>
                    <TextInput
                        name="firstname"
                        type="text"
                        placeholder="Firstname..."
                        label="Имя"
                    />
                </div>
                <div>
                    <TextInput
                        name="lastname"
                        type="text"
                        placeholder="Lastname..."
                        label="Фамилия"
                    />
                </div>
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
                <div>
                    <TextInput
                        name="repeatPassword"
                        type="password"
                        placeholder="Repeat password..."
                        label="Подтверждение пароля"
                    />
                </div>
                <div>
                    <TextInput
                        name="tgId"
                        type="number"
                        placeholder="Telegram ID..."
                        label="Ваш ID Telegram"
                    />
                </div>
                <div className={classes.description}>
                    Получить ID можно через нашего телеграм бота @tenzor_scaner_bot
                </div>
                <button type="submit" className={classes.button}>
                    Зарегистрироваться
                </button>
            </Form>
        </Formik>
    );
}

export default RegisterForm;