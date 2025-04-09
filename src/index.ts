import { WeatherService } from './weatherService';

const weatherService = new WeatherService();

// Example usage
async function main() {
    try {
        const forecast = await weatherService.getForecast(39.7456, -97.0892);
        console.log('Weather forecast:', forecast);
    } catch (error) {
        console.error('Error:', error);
    }
}

main();