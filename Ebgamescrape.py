import requests
import bs4
import time
import os
from bs4 import BeautifulSoup as Bsoup

print ("What do you want to search for on EbGames:")
sea = input (":")

url = "https://ebgames.com.au/search?q=" + (sea)
resp = requests.get(url)
soup = Bsoup(resp.text, 'html.parser')
platforms = soup.select(".product-top-level-group")
price = soup.select(".price")
names = soup.select(".product-title")
stripped_names = [na.text.strip() for na in names]
stripped_prices = [pri.text.strip() for pri in price]
stripped_platforms = [plat.text.strip() for plat in  platforms]




Game = {
    game[0]: {
        "Price": game[1],
        "Platform": game[2]
    } for game in zip(
        stripped_names,
        stripped_prices,
        stripped_platforms,
    )
}

for Gamename, Gameinfo in Game.items():
    print(Gamename)
    print("Platform:", Gameinfo['Platform'])
    print("Price:", Gameinfo['Price'])
    print("\n")

os.system('pause')
