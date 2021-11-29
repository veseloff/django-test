import Cookies from 'js-cookie';

export const businessTripsAPI = {
    async getBusinessTrips(userId) {
        return await fetch(`/account/all_business_trip?userId=${userId}`)
            .then(response => response.json())
            .then(data => data)
            .catch(error => console.error(error))
    },
    async getBusinessTripInfo(idBT) {
        return await fetch(`/account/info_business_trip?idBT=${idBT}`)
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
    async putBusinessTrips(idBT, bt) {
        const url = '/account/update_business_trip/';
        const csrftoken = Cookies.get('csrftoken');
        return await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({idBT, bt}),
        }).then(response => response.json())
            .then(data => data)
            .catch(error => console.error(error))
    },
    async deleteBusinessTrips(idBT) {
        const url = '/account/delete_business_trip/';
        const csrftoken = Cookies.get('csrftoken');
        return await fetch(url, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({idBT}),
        }).then(response => response.text())
            .then(data => data)
            .catch(error => console.error(error))
    },
    async postHotelInfo(info) {
        const url = '/account/create_hotel/';
        const csrftoken = Cookies.get('csrftoken');
        return await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(info),
        }).then(response => response.json())
            .then(data => data)
            .catch(error => console.error(error))
    },
    async putHotelInfo(info) {
        const url = '/account/update_hotel/';
        const csrftoken = Cookies.get('csrftoken');
        return await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json; charset=utf-8',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(info),
        }).then(response => response.json())
            .then(data => data)
            .catch(error => console.error(error))
    },
}

export const hotelsAPI = {
    async getHotels(city, offset, star, option, checkIn, checkOut) {
        const url = `/hotel/hotels_${option}?city=${city}&offset=${offset}&star=${star}&check_in=${checkIn}&check_out=${checkOut}`;
        return await fetch(url)
            .then(response => response.json())
            .then(data => data)
            .catch(error => console.error(error))
    },
}
