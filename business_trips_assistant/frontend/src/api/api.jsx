import Cookies from 'js-cookie';

export const businessTripsAPI = {
    async getBusinessTrips(userId) {
        return await fetch(`/account/all_business_trip?userId=${userId}`)
            .then(response => response.json())
            .then(data => data)
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
