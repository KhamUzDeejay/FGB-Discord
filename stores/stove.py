import requests
from bs4 import BeautifulSoup

URL = "https://store.onstove.com/en/store"

def get_games():
    games = []
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    for g in soup.select(".game-card"):
        price = g.select_one(".price")
        if price and "FREE" in price.text.upper():
            games.append({
                "id": g["data-id"],
                "name": g.select_one(".title").text,
                "store": "Stove",
                "end": None,
                "price": 0,
                "free_type": "free",
                "url": "https://store.onstove.com",
                "image": g.select_one("img")["src"]
            })
    return games
