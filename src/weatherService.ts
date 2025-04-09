import axios from 'axios';

export class WeatherService {
    private baseUrl = 'https://api.weather.gov';

    async getForecast(latitude: number, longitude: number) {
        try {
            // Get the grid point for the coordinates
            const pointResponse = await axios.get(`${this.baseUrl}/points/${latitude},${longitude}`);
            const { gridId, gridX, gridY } = pointResponse.data.properties;

            // Get the forecast using the grid point
            const forecastResponse = await axios.get(
                `${this.baseUrl}/gridpoints/${gridId}/${gridX},${gridY}/forecast`
            );

            return forecastResponse.data.properties.periods;
        } catch (error) {
            console.error('Error fetching weather data:', error);
            throw error;
        }
    }
}