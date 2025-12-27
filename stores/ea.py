import requests
from bs4 import BeautifulSoup

URL = "https://www.ea.com/games/library"

def get_games():
    games = []
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    for g in soup.select("article"):
        if "free" in g.text.lower():
            games.append({
                "id": g.text,
                "name": g.text.strip(),
                "store": "EA",
                "end": None,
                "price": 0,
                "free_type": "subscription",
                "url": "https://www.ea.com",
                "image": "https://ea.com/logo.png"
            })
    return games
