import bs4
import requests
import random

INFO = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 OPR/121.0.0.0"}

def make_html(url):
    response = requests.get(url, headers=INFO)
    html = bs4.BeautifulSoup(response.text, 'lxml')
    return html

def main():
    i = 1
    while i <= 343:
        url = f"https://kinoukr.tv/films/page/{i}"
        html = make_html(url)
        print(html)
        films = html.find_all("div", class_="short clearfix with-mask")
        for film in films:
            name = film.find("a", class_="short-title")
            print(name.text)
        i += 1

if __name__ == "__main__":
    main()