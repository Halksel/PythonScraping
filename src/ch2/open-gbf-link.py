from bs4 import BeautifulSoup
import lxml.html

html = open('test.html', encoding='utf-8').read()
dom = lxml.html.fromstring(html)

for o in dom.xpath(u"/html/body/table/tbody/tr/td[2]/div[2]/ul[1]/li[1]/ul"):
    print(o)
