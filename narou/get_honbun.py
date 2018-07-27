from lxml import html
import requests

url = requests.get("https://ncode.syosetu.com/n6470bm/1/").content
url = html.fromstring(url)

honbun = url.xpath('string(//*[@id="novel_honbun"])')

print(honbun)
