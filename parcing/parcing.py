import bs4
import requests

url = "https://scrapingclub.com/exercise/list_basic/"

# response = requests.get(url)


link1 = 2

for link in range(2, 7):
    url = f"https://scrapingclub.com/exercise/list_basic/?page={link}"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "lxml")
    cards = soup.find_all("div", class_="w-full rounded border")
    for card in cards:
        name = card.find("h4").find("a")
        price = card.find("h5")
        print(f"{name.text}-{price.text}")