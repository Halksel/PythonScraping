from lxml import etree, html
import requests
import pickle
import os
import time
import urllib
from typing import List, Dict


def download_image(url, dst_path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(dst_path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)


def dump_node(node, indent=0):
    print("{}{} {} {} {}".format('  ' * indent, node.tag, node.attrib,
                                 node.text, node.tail))
    #     print(html.tostring(node).decode())
    for child in node:
        dump_node(child, indent + 1)


def getTextWithoutNone(elem):
    if elem is None:
        return
    return elem.text


imgPath: str = '../datas/img/weapons'
os.makedirs('../datas/img/weapons', exist_ok=True)


def getWeaponData(root, sleep_time_sec) -> Dict[str, List[str]]:
    dic: Dict[str, List[str]] = {}
    for node in root:
        lis: List[str] = []
        url = node.xpath("td[1]/a")[0].attrib['href']
        name = getTextWithoutNone(node.xpath("td[2]")[0])
        if name is None or name[0] == '[':
            if node.find("td[2]/a") is not None:
                name = getTextWithoutNone(node.xpath("td[2]/a")[0])
            elif node.find("td[2]/br") is not None:
                name = node.xpath("td[2]/br")[0].tail
        try:
            attr = getTextWithoutNone(node.xpath("td[3]/span")[0])
        except:
            attr = ""
        lis.append(attr)
        kind = getTextWithoutNone(node.xpath("td[4]")[0])
        lis.append(kind)
        skill = getTextWithoutNone(node.xpath("td[7]/a")[0])
        lis.append(skill)
        savename = imgPath + "/" + name + ".png"
        dic[name] = lis
        #     download_image(url, savename)
        #     time.sleep(sleep_time_sec)
    return dic


parser = etree.HTMLParser(recover=True)
html_text = requests.get("http://gbf-wiki.com/index.php?%C9%F0%B4%EFSSR").text
root = html.fromstring(html_text)
trs = root.xpath("/html/body/table/tr/td[2]/div[2]/div[5]/table/tbody/tr")

print("武器名,属性,武器種,スキル,")
dic: Dict[str, List[str]] = {}
dic = getWeaponData(trs, 0.2)
print(len(dic))
with open("../datas/pickles/weapon.pickle", 'wb') as f:
    pickle.dump(dic, f)
