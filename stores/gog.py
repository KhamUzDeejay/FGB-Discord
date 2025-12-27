import requests

URL = "https://www.gog.com/games/ajax/filtered?price=free"

def get_games():
    games = []
    data = requests.get(URL).json()

    for g in data["products"]:
        games.append({
            "id": str(g["id"]),
            "name": g["title"],
            "store": "GOG",
            "end": None,
            "price": g["price"]["baseAmount"],
            "url": "https://www.gog.com" + g["url"],
            "image": "https:" + g["image"] + ".jpg"
        })
    return games
