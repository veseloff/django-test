function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

export const businessTripsAPI = {
    async getBusinessTrips() {
        return await fetch('http://127.0.0.1:8000/account/all_business_trip/')
            .then(response => response.json())
            .then(data => data)
            .catch(error => console.error(error))
    },
    async postBusinessTrips(bt) {                                                    //todo: VsALT - post запрос на бэк
        const url = 'http://127.0.0.1:8000/account/create_business_trip/';
        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    "Accept": "application/json",
                    'Content-Type':'application/json',
                    //'Content-Type': 'application/json;charset=utf-8',
                    //'X-CSRFToken': csrftoken,
                    //'Access-Control-Allow-Credentials': true
                },
                body: JSON.stringify(bt),
                //credentials: 'include'
            });
            const json = await response.json();
            console.log('Успех:', JSON.stringify(json));
        } catch (error) {
            console.error('Ошибка:', error);
        }
    },
}
