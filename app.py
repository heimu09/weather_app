from flask import Flask, render_template, request, jsonify, session
from weather_api import get_weather, get_city_info
from database import init_db, save_search, get_history, get_city_stats
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    last_city = session.get('last_city')
    return render_template('index.html', last_city=last_city)


@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    city_info = get_city_info(city)

    if city_info and 'results' in city_info and len(city_info['results']) > 0:
        latitude = city_info['results'][0]['latitude']
        longitude = city_info['results'][0]['longitude']
        weather_data = get_weather(latitude, longitude)
        
        if weather_data:
            session['last_city'] = city
            save_search(city)
            return jsonify({"weather_data": weather_data, "city_info": city_info})
        
    return jsonify({"error": "Could not retrieve weather data"}), 400


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    if search:
        city_info = get_city_info(search, count=5)
        if city_info and 'results' in city_info:
            cities = [result['name'] for result in city_info['results']]
            return jsonify(cities)
    return jsonify([])


@app.route('/history')
def history():
    return jsonify(get_history())


@app.route('/stats')
def stats():
    return jsonify(get_city_stats())


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
