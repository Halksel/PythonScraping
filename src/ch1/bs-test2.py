from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id="title">スクレイピングとは</h1>
    <p>Webページの解析</p>
    <p id="body">任意の箇所の抽出</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find(id="title")
body = soup.find(id="body")

print(title)
print(body)
