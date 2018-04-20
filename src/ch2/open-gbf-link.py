from lxml import html
import requests

page = requests.get(
    "http://gbf-wiki.com/index.php?%BF%CD%CA%AA%C9%BE%B2%C1SSR")

page.raise_for_status()

root = html.fromstring(page.text)
# /html/body/table/tbody/tr/td[2]/div[2]/ul[1]/li[1]/a

xpath = '/html/body/table/tbody/tr/td[2]/div[2]/ul[1]/li[1]'


# uls = root.xpath(xpath)
#
# print(xpath)
# for ul in uls:
#     print(ul.text_content())
