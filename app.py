import os
import requests
from flask import Flask, Response, request

app = Flask(__name__)

# ✅ Your custom login credentials
USERNAME = "Prajwal_07"
PASSWORD = "prajwal@5211134"

def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return Response(
        'Access Denied\n', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

@app.route('/vod.m3u')
def serve_vod():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()

    # Fetch Movies + Series
    movies_url = os.environ.get('MOVIES_URL')
    series_url = os.environ.get('SERIES_URL')

    movies = requests.get(movies_url).text if movies_url else ''
    series = requests.get(series_url).text if series_url else ''

    # Merge while removing duplicate header lines
    merged = "#EXTM3U\n"
    if "#EXTM3U" in movies:
        merged += movies.strip().split('\n', 1)[1] + '\n'
    if "#EXTM3U" in series:
        merged += series.strip().split('\n', 1)[1]

    return Response(merged, mimetype='application/x-mpegURL')

@app.route('/')
def index():
    return '✅ VOD playlist is hosted at /vod.m3u (login required)'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
