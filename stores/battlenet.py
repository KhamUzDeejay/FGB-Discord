import requests
from bs4 import BeautifulSoup

URL = "https://news.blizzard.com/en-us"

def get_games():
    games = []
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    for a in soup.select("a"):
        if "free" in a.text.lower():
            games.append({
                "id": a["href"],
                "name": a.text.strip(),
                "store": "Battle.net",
                "end": None,
                "price": 0,
                "free_type": "weekend",
                "url": a["href"],
                "image": "https://blizzard.com/logo.png"
            })
    return games
