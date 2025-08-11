import bs4
import requests
import json

url = "https://www.ctrs.com.ua/smartfony/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(response.content, "lxml")  #content == code(html)
json_file = soup.find("script")
data = json.loads(json_file.text)      #load == laden
for a in data["itemListElement"]:
    print(a["name"])
    print("-")
    print(a["offers"]["price"])