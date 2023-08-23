from flask import Flask, render_template
import urllib.request, json
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


tmdb_api_key = os.getenv('TMDB_API_KEY')


@app.route("/")
def hello_world():

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={tmdb_api_key}"

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template('home.html', movies=dict["results"])




if __name__ == "__main__":
    app.run(debug=True)