import pandas as pd
import csv
import re

mycsv = csv.reader(
    open('armData-ssr.txt', 'r', encoding="utf-8"), delimiter="|")

attributeMatchObj = re.compile(r"(火|風|水|土|光|闇|全)")
skillMatchObj = re.compile(r"\[\[(.*)>")

rows = []
for row in mycsv:
    newrow = []
    for r in row[2:20]:
        newrow.append(str(r).encode('shift-jis', 'ignore').decode('shift-jis'))
    attribute = attributeMatchObj.search(str(newrow[1]))
    newrow[1] = attribute.group(1) if attribute != None else None
    newrow[5] = skillMatchObj.search(str(newrow[5])).group(1)
    secondSkill = skillMatchObj.search(str(newrow[6]))
    newrow[6] = secondSkill.group(1) if secondSkill != None else None
    rows.append(newrow)

df = pd.DataFrame(
    rows,
    columns=[
        '武器名', '属性', '武器種', '最大レベル', '奥義', '第一スキル', '第二スキル', '最小HP', '最小ATK',
        '最大HP', '最大ATK', 'info', '入手法', '凸上限', '100LvHP', '100LvATK',
        '150LvHP', '150LvATK'
    ])
df.to_csv("armData.csv", encoding="shift-jis")
