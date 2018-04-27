from lxml import html
from bs4 import BeautifulSoup
import re
import pandas as pd

with open("imas.html", "r") as f:
    soup = f.read()

root = html.fromstring(soup)

count = 183  # imas の人数

result = pd.DataFrame(data=None, index=None, columns=['b', 'w', 'h'])

for i in range(count):
    name = root.xpath(
        '/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[5]/table/tbody/tr['
        + str(i + 1) + ']/td[1]/a')[0]
    b = root.xpath(
        '/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[5]/table/tbody/tr['
        + str(i + 1) + ']/td[2]')[0].text
    w = root.xpath(
        '/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[5]/table/tbody/tr['
        + str(i + 1) + ']/td[3]')[0].text
    h = root.xpath(
        '/html/body/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[5]/table/tbody/tr['
        + str(i + 1) + ']/td[4]')[0].text
    name = re.sub(r'\s', '', name.text_content())
    b = re.sub(r'\s', '', b)
    w = re.sub(r'\s', '', w)
    h = re.sub(r'\s', '', h)
    result.loc[name] = [b, w, h]

result.to_csv("imas.csv",encoding="shift_jis")
