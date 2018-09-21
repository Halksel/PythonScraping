from lxml import html
import requests
from typing import List, Dict, Tuple, TypeVar, Set
from selenium import webdriver
import time


def get_cite_count(url: str):
    driver = webdriver.Firefox()
    driver.get(url)
    count: int = driver.find_elements_by_xpath('//*[@id="almCitations"]')[
        0].text.split('\n')[0]
    texts: List[str] = []
    for i in range(1, 5):
        text: str = driver.find_elements_by_xpath(
            '//*[@id="section' + str(i) + '"]')[0].text
        texts.append(text)
    ref_root = driver.find_elements_by_xpath(
        '/html/body/main/div/section/div/div[3]/div/div[11]/ol')[0]
    for ref in ref_root.find_elements_by_xpath("//*[contains(@id,'ref')]"):
        arr = ref.text.split('\n')
        if len(arr) > 1:
            paper_num = arr[0]
            paper_title = arr[1]
            print(paper_num, paper_title)


#     paper_title = driver.find_elements_by_xpath('//*[@id="ref1"]')[
#         0].text.split('\n')[1]
#     address = driver.find_element_by_xpath(
#         "/html/body/main/div/section/div/div[3]/div/div[11]/ol/li[1]/ul/li[3]/a"
#     ).get_attribute("href")
#     cited_count = get_cited(address)
    time.sleep(1)
    driver.close()
    driver.quit()


def get_cited(address: str) -> int:
    url = requests.get(address).content
    url = html.fromstring(url)

    cited_count = url.xpath(
        "/html/body/div[1]/div[11]/div[2]/div[2]/div[2]/div/div/div[3]/a[3]")[
            0].text.split(' ')[2]
    return cited_count


get_cite_count(
    "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0202580"
)
