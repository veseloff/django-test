import Cookies from 'js-cookie';

/*function getCookie(name) {
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
}*/

//const csrftoken = getCookie('csrftoken');

export const businessTripsAPI = {
    async getBusinessTrips() {
        return await fetch('/account/all_business_trip/')
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error(error))
    },
    async getCsrf() {
        return await fetch('/account/get_csrf/')
            .then(response => response.text())
            .then(data => data)
            .catch(error => console.error(error))
    },
    async postBusinessTrips(bt) {
        const url = '/account/create_business_trip/';
        const csrftoken = Cookies.get('csrftoken');
        return await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(bt),
        }).then(response => response.json())
            .then(data => data)
            .catch(error => console.error(error))
    },
    async deleteBusinessTrips(id) {
        const url = '/account/create_business_trip/';
        const csrftoken = Cookies.get('csrftoken');
        return await fetch(url, {
            method: 'DELETE',
            //mode: 'same-origin',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'X-CSRFToken': csrftoken,
                //'Access-Control-Allow-Credentials': true,
            },
            body: JSON.stringify(id),
            //credentials: 'include',
        }).then(response => response.text())
            .then(data => data)
            .catch(error => console.error(error))
    },
}
