from bs4 import BeautifulSoup
import requests
import urllib3

r = requests.get("https://imascg-slstage.boom-app.wiki/entry/idol-measurements")

html = r.text

soup = BeautifulSoup(html, "html.parser")

with open('imas.html', mode='w', encoding='utf-8') as fw:
    fw.write(soup.prettify())
