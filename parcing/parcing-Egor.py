import bs4
import requests

def parse_description(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "lxml")
    description = soup.find('p', class_='card-description').text
    return description

num = 1
for link in range(1, 7):
    if link == 1:
        url = "https://scrapingclub.com/exercise/list_basic/"
    else:
        url = f"https://scrapingclub.com/exercise/list_basic/?page={link}"
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "lxml")
    cards = soup.find_all("div", class_="w-full rounded border")
    for card in cards:
        name = card.find("h4").find("a")
        price = card.find("h5")
        href = card.find("h4").find("a").get('href')
        href_ready = f'https://scrapingclub.com{href}'
        description = parse_description(href_ready)
        # print(href_ready)
        print(f"{num}. {name.text}-{price.text}")
        print(description, end='\n\n')
        num += 1
        
