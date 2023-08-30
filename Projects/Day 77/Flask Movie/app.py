import os, requests, urllib.request, json, bcrypt
from flask import Flask, render_template, request, jsonify, redirect, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import UserMixin


load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = os.getenv('DATABASE_KEY')

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

with app.app_context():
    db.create_all()


TMDB_ACCESS_KEY = os.getenv('TMDB_ACCESS')
TMDB_API_KEY = os.getenv('TMDB_API_KEY')


GENRE_DATA = [
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

def make_tmdb_request(url):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_ACCESS_KEY}"
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        response = urllib.request.urlopen(req)
        if response.status == 200:
            data = response.read()
            data_dict = json.loads(data)
            return data_dict
        else:
            return None
        
    except urllib.error.URLError as e:
        print(e)
        return None


@app.route("/")
def home():
    if 'username' in session:
        url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
        data_dict = make_tmdb_request(url)
        if data_dict:
            return render_template('home.html', movies=data_dict["results"], User = session['username'])
        else:
            return "Request failed"
    return render_template('login.html')




@app.route('/genre/<int:id>')
def genre_id(id):
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres={id}"
    data_dict = make_tmdb_request(url)
    
    if data_dict:
        genre_name = next((genre["name"] for genre in GENRE_DATA if genre["id"] == id), None)
        return render_template('genre_id.html', movies=data_dict["results"], main_genre_name=genre_name)
    else:
        return "Request failed"


@app.route('/movie/<int:id>')
def movie_id(id):
    url_movie = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    url_cast = f"https://api.themoviedb.org/3/movie/{id}/credits?language=en-US"

    data_dict_movie = make_tmdb_request(url_movie)
    data_dict_cast = make_tmdb_request(url_cast)

    if data_dict_movie and data_dict_cast:
        return render_template('movie.html', movie_detail=data_dict_movie, cast_detail=data_dict_cast['cast'])
    else:
        return "Request failed"


@app.route('/search-movies')
def search_movies():
    search_query = request.args.get('query')

    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={search_query}'

    response = requests.get(url)

    if response.ok:
        movie_data = response.json()
        return render_template('search.html', movies=movie_data['results'])
    else:
        return render_template('search.html', movies=[], error='Failed to fetch movie data from TMDb')



@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username = username).first()

        if user and user.check_password(password):
            session['username'] = user.username
            return redirect('/')
        else:
            return render_template('login.html', error = "invalid Information")

    return render_template('login.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        new_user = User(username=username, password=password)

        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    
    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
