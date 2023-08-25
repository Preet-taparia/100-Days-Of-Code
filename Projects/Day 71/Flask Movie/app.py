from flask import Flask, render_template
import urllib.request, json
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

tmdb_api_key = os.getenv('TMDB_API_KEY')

@app.route("/")
def hello_world():
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer <API_KEY>"
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






if __name__ == "__main__":
    app.run(debug=True)
