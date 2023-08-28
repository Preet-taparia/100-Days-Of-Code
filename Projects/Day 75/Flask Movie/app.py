from flask import Flask, render_template, redirect, jsonify, url_for, request
import urllib.request, json
from dotenv import load_dotenv
import os
import requests

load_dotenv()
app = Flask(__name__)

tmdb_access_key = os.getenv('TMDB_ACCESS')
tmdb_api_key = os.getenv('TMDB_API_KEY')



genre_data = [
    {"id": 28, "name": "Action"},
    {"id": 12, "name": "Adventure"},
    {"id": 16, "name": "Animation"},
    {"id": 35, "name": "Comedy"},
    {"id": 80, "name": "Crime"},
    {"id": 99, "name": "Documentary"},
    {"id": 18, "name": "Drama"},
    {"id": 10751, "name": "Family"},
    {"id": 14, "name": "Fantasy"},
    {"id": 36, "name": "History"},
    {"id": 27, "name": "Horror"},
    {"id": 10402, "name": "Music"},
    {"id": 9648, "name": "Mystery"},
    {"id": 10749, "name": "Romance"},
    {"id": 878, "name": "Science Fiction"},
    {"id": 10770, "name": "TV Movie"},
    {"id": 53, "name": "Thriller"},
    {"id": 10752, "name": "War"},
    {"id": 37, "name": "Western"}
]




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
    



@app.route('/genre/<int:id>')
def genre_id(id):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={id}"
    
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
            
            # Find the genre name corresponding to the provided ID
            genre_name = None
            for genre in genre_data:
                if genre["id"] == id:
                    genre_name = genre["name"]
                    break
            
            return render_template('genre_id.html', movies=data_dict["results"], main_genre_name=genre_name)
            
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
