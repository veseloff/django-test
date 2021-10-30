export const businessTripsAPI = {
    async getBusinessTrips() {
        const response = fetch('http://127.0.0.1:8000/account/all_business_trip/', {
            method: 'GET', // *GET, POST, PUT, DELETE, etc.
            mode: 'no-cors', // no-cors, *cors, same-origin
            headers: {'Content-Type': 'application/json'}
        }).then((response) => {
            console.log(response)
            return response;
        });
        return await response;

        /*.then((response) => {
            console.log(response)
            return response.json();
        })*//*
            .then((data) => {
                console.log(data);
            });*/
    },
}
