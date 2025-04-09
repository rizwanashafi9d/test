from typing import Dict, List
from dataclasses import dataclass

@dataclass
class WeatherPeriod:
    name: str
    temperature: int
    temperature_unit: str
    short_forecast: str
    detailed_forecast: str

class AndroidWeatherClient:
    def __init__(self, weather_service):
        self.weather_service = weather_service

    def get_formatted_forecast(self, latitude: float, longitude: float) -> List[WeatherPeriod]:
        """Get weather forecast formatted for Android display"""
        try:
            raw_forecast = self.weather_service.get_forecast(latitude, longitude)
            return [
                WeatherPeriod(
                    name=period['name'],
                    temperature=period['temperature'],
                    temperature_unit=period['temperatureUnit'],
                    short_forecast=period['shortForecast'],
                    detailed_forecast=period['detailedForecast']
                )
                for period in raw_forecast
            ]
        except Exception as e:
            print(f'Error formatting weather data for Android: {str(e)}')
            raise

    def get_weather_notification_text(self, weather_period: WeatherPeriod) -> str:
        """Generate notification text for weather alerts"""
        return f'{weather_period.name}: {weather_period.temperature}°{weather_period.temperature_unit} - {weather_period.short_forecast}'

def main():
    # Example usage with the WeatherService
    from app import WeatherService
    
    weather_service = WeatherService()
    android_client = AndroidWeatherClient(weather_service)
    
    try:
        # Example coordinates (Kansas, USA)
        forecast = android_client.get_formatted_forecast(39.7456, -97.0892)
        print('Android Weather Notifications:')
        for period in forecast:
            notification_text = android_client.get_weather_notification_text(period)
            print(notification_text)
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()