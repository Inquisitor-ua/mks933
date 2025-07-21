import bs4
import requests

url = "https://www.ctrs.com.ua/smartfony/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(response.content, "lxml")  #content == code(html)
print(soup)
