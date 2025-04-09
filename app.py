import requests
from typing import Dict, List

class WeatherService:
    def __init__(self):
        self.base_url = 'https://api.weather.gov'

    def get_forecast(self, latitude: float, longitude: float) -> List[Dict]:
        try:
            # Get the grid point for the coordinates
            point_response = requests.get(f'{self.base_url}/points/{latitude},{longitude}')
            point_data = point_response.json()
            properties = point_data['properties']

            # Get the forecast using the grid point
            forecast_url = f'{self.base_url}/gridpoints/{properties["gridId"]}/{properties["gridX"]},{properties["gridY"]}/forecast'
            forecast_response = requests.get(forecast_url)
            forecast_data = forecast_response.json()

            return forecast_data['properties']['periods']

        except Exception as e:
            print(f'Error fetching weather data: {str(e)}')
            raise

def main():
    weather_service = WeatherService()
    try:
        # Example coordinates (Kansas, USA)
        forecast = weather_service.get_forecast(39.7456, -97.0892)
        print('Weather forecast:')
        for period in forecast:
            print(f'{period["name"]}: {period["shortForecast"]}, Temperature: {period["temperature"]}°{period["temperatureUnit"]}')
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()