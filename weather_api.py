import requests


def get_city_info(city: str, count: int = 1, language: str = 'ru', format: str = 'json') -> dict:
    try:
        url = 'https://geocoding-api.open-meteo.com/v1/search'
        params = {
            'name': city,
            'count': count,
            'language': language,
            'format': format
        }
        response = requests.get(url, params)
        data = response.json()
        return data

    except Exception as e:
        print(f'Error fetching city data: {e}')
        return None

def get_weather(latitude: float, longitude: float, current: str = 'temperature_2m') -> dict:
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": current
        }
        response = requests.get(url, params)
        data = response.json()
        return data

    except Exception as e:
        print(f'Error fetching weather data: {e}')
        return None


if __name__ == "__main__":
    city_info = get_city_info("Karaganda")
    weather = get_weather(city_info['results'][0]['latitude'], city_info['results'][0]['longitude'])
    print(weather)
