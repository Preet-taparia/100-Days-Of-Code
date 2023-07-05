import requests
from bs4 import BeautifulSoup

url = "https://www.entoin.com/entertainment/best-anime-to-watch"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

all_anime = soup.find_all(name = "strong")
anime_titles = [anime.getText() for anime in all_anime]
animes= anime_titles[::-1]

with open("animes.txt", mode = "w") as file:
    for anime in animes:
        file.write(f"{anime}\n")