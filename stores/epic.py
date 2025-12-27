import requests
from dateutil import parser

URL = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"

def get_games():
    games = []
    data = requests.get(URL).json()

    for g in data["data"]["Catalog"]["searchStore"]["elements"]:
        price = g["price"]["totalPrice"]
        if price["discountPrice"] == 0:
            promo = g["promotions"]["promotionalOffers"][0]["promotionalOffers"][0]
            games.append({
                "id": g["id"],
                "name": g["title"],
                "store": "Epic Games",
                "end": parser.parse(promo["endDate"]),
                "price": price["originalPrice"] / 100,
                "url": f"https://store.epicgames.com/p/{g['productSlug']}",
                "image": g["keyImages"][0]["url"]
            })
    return games
