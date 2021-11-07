export const businessTripsAPI = {
    async getBusinessTrips() {
        return await fetch('http://127.0.0.1:8000/account/all_business_trip/')
            .then(response => response.json()) // преобразуем ответ в json
            .then(data => data)
            .catch(error => console.error(error))
    }
}
