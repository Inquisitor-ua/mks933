import bs4
import requests

url = 'https://quotes.toscrape.com'

work = requests.Session()

work.get(url)
response = work.get('https://quotes.toscrape.com/login')
soup = bs4.BeautifulSoup(response.text, 'lxml')
csrf = soup.find('form').find('input').get('value')

data_my = {'csrf_token': csrf, 'username': 'hello', 'password': 'world'}

response = work.post('https://quotes.toscrape.com/login', data=data_my)
print(response.text)