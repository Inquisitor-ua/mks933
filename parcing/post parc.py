import bs4       #basis
import requests  #anfragen...

url = "https://quotes.toscrape.com"

work = requests.Session() #merken

work.get(url) #anfrage
response = work.get("https://quotes.toscrape.com/login")
soup = bs4.BeautifulSoup(response.text, "lxml")  #content == code(html)
csrf = soup.find("form").find("input").get("value")
print(csrf)

data_my = {"csrf_token": csrf, "username": "hello", "password": "world"}
response = work.post("https://quotes.toscrape.com/login", data=data_my)
print(response.text)