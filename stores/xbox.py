import requests
from bs4 import BeautifulSoup

URL = "https://www.xbox.com/en-US/games/free-play-days"

def get_games():
    games = []
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    for g in soup.select("a"):
        if "Free Play Days" in g.text:
            games.append({
                "id": g["href"],
                "name": g.text.strip(),
                "store": "Xbox (Console/PC)",
                "end": None,
                "price": 0,
                "free_type": "subscription",
                "url": "https://www.xbox.com" + g["href"],
                "image": "https://xbox.com/logo.png"
            })
    return games
