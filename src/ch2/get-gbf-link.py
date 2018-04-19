from bs4 import BeautifulSoup
import requests
import urllib3

r = requests.get("http://gbf-wiki.com/index.php?%BF%CD%CA%AA%C9%BE%B2%C1SSR")

html = r.text

soup = BeautifulSoup(html, "html.parser")

with open('test.html', mode='w', encoding='utf-8') as fw:
    fw.write(soup.prettify())

