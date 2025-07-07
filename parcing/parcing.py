import bs4       #basis..
import requests  #anfragen..

num = 1
for link in range(1, 7):
    if link == 1:
        url = "https://scrapingclub.com/exercise/list_basic/"
    else:
        url = f"https://scrapingclub.com/exercise/list_basic/?page={link}"
    response = requests.get(url)  #anfragen..
    soup = bs4.BeautifulSoup(response.content, "lxml")  #content == code(html)
    cards = soup.find_all("div", class_="w-full rounded border")
    for card in cards:
         name = card.find("h4").find("a").get("href")
         price = card.find("h5")
         print(f"{num}. {name.text}-{price.text}")
         num += 1