import unittest
from app import app, init_db


class WeatherAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        init_db()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_weather(self):
        response = self.app.post('/weather', data=dict(city='Karaganda'))
        self.assertEqual(response.status_code, 200)
        response_json = response.get_json()
        self.assertIsNotNone(response_json)
        self.assertIn('weather_data', response_json)
        self.assertIn('city_info', response_json)
        self.assertIn('latitude', response_json['city_info']['results'][0])
        self.assertIn('longitude', response_json['city_info']['results'][0])
        self.assertIn('current_weather', response_json['weather_data'])

    def test_history(self):
        response = self.app.get('/history')
        self.assertEqual(response.status_code, 200)

    def test_stats(self):
        response = self.app.get('/stats')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
