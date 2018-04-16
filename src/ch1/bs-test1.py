from bs4 import BeautifulSoup

html = """
<html><body>
    <h1>スクレイピングとは</h1>
    <p>Webページの解析</p>
    <p>任意の箇所の抽出</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
print(h1.string, p1.string, p2.string)
