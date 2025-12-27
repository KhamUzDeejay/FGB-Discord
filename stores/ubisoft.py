import requests
from bs4 import BeautifulSoup

URL = "https://www.ubisoft.com/en-us/help/gameplay/article/free-weekends/000065990"

def get_games():
    games = []
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")

    for li in soup.select("li"):
        text = li.text.lower()
        if "free" in text:
            games.append({
                "id": text,
                "name": li.text.strip(),
                "store": "Ubisoft",
                "end": None,
                "price": 0,
                "free_type": "weekend",
                "url": "https://www.ubisoft.com",
                "image": "https://static.ubisoft.com/ubisoft-logo.png"
            })
    return games
