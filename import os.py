import os
import requests
from flask import Flask, Response

app = Flask(__name__)

@app.route('/vod.m3u')
def serve_vod():
    # Fetch Movies + Series from Starshare
    movies_url = os.environ.get('MOVIES_URL')
    series_url = os.environ.get('SERIES_URL')

    movies = requests.get(movies_url).text if movies_url else ''
    series = requests.get(series_url).text if series_url else ''

    # Merge both playlists, removing the second #EXTM3U
    merged = "#EXTM3U\n"
    if "#EXTM3U" in movies:
        merged += movies.strip().split('\n', 1)[1] + '\n'
    if "#EXTM3U" in series:
        merged += series.strip().split('\n', 1)[1]

    return Response(merged, mimetype='application/x-mpegURL')

@app.route('/')
def index():
    return '✅ Public VOD playlist is hosted at /vod.m3u'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
