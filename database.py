import sqlite3


def init_db():
    conn = sqlite3.connect('weather_app.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS searches
                 (id INTEGER PRIMARY KEY, city TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()


def save_search(city):
    conn = sqlite3.connect('weather_app.db')
    c = conn.cursor()
    c.execute('INSERT INTO searches (city) VALUES (?)', (city,))
    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect('weather_app.db')
    c = conn.cursor()
    c.execute('SELECT city, timestamp FROM searches ORDER BY timestamp DESC')
    history = c.fetchall()
    conn.close()
    return history


def get_city_stats():
    conn = sqlite3.connect('weather_app.db')
    c = conn.cursor()
    c.execute('SELECT city, COUNT(city) as count FROM searches GROUP BY city')
    stats = c.fetchall()
    conn.close()
    return stats
