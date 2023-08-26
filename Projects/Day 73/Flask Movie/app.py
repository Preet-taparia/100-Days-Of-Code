from flask import Flask, render_template, redirect, jsonify, url_for, request
import urllib.request, json
from dotenv import load_dotenv
import os
import requests

load_dotenv()
app = Flask(__name__)

tmdb_access_key = os.getenv('TMDB_ACCESS')
tmdb_api_key = os.getenv('TMDB_API_KEY')








@app.route("/")
def home():

    url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {tmdb_access_key}"
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        response = urllib.request.urlopen(req)
        
        if response.status == 200:
            data = response.read()
            data_dict = json.loads(data)
            #print(type(data_dict['results']))
            return render_template('home.html', movies=data_dict["results"])
            
        else:
            return f"Request failed with status code {response.status}"
    
    except urllib.error.URLError as e:
        print(e)

    return f"Error: {e}"
    


@app.route('/movie/<int:id>')
def movie_id(id):
    
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {tmdb_access_key}"
    }
    
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read()
    data_dict = json.loads(data)
    return render_template('movie.html', movie_detail=data_dict)


@app.route('/search-movies')
def search_movies():
    search_query = request.args.get('query')

    url = f'https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={search_query}'

    response = requests.get(url)

    if response.ok:
        movie_data = response.json()
        return jsonify(movie_data)
    else:
        return jsonify({'error': 'Failed to fetch movie data from TMDb'}), 500
    
@app.route('/find_movies')
def find_movies():
    return render_template('Find.html')

if __name__ == "__main__":
    app.run(debug=True)
