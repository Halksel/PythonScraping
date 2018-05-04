import urllib.request
from lxml import html
import sys

keyword = "haskell"
resp = urllib.request.urlopen(
    'https://qiita.com/Trickey/items/28f2aaddfe32a0035628').read()

root = html.fromstring(resp)

xpath = '/html/body/div[2]/article/div[1]/div/div[2]/div/div[1]/h1'
print(root.xpath(xpath)[0].text)
