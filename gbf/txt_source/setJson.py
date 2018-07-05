import json
import sys

args = sys.argv


def setParameters(colsName, string, answerList, dic):
    print(string + " :" + answerList)
    dic[colsName] = input()


fileObj = open(args[1], 'w') templeteObj = open('hensei.json', 'r')

data = json.load(templeteObj)

dicDjeeta = {}
setParameters("Rank", "Rankを入力してください", "1 ~ 225", dicDjeeta)
setParameters("ジョブ", "Jobを入力してください", "", dicDjeeta)
setParameters("マスボ", "攻撃のマスボを入力してください", "1 ~ 18", dicDjeeta)
setParameters("属性", "属性を入力してください", "火水風土光闇", dicDjeeta)
setParameters("有利", "敵は有利属性ですか？", "1(敵の弱点をつける) or 0(1以外)", dicDjeeta)
setParameters("敵防御", "敵の防御値を入力してください", "デフォは10", dicDjeeta)

dicSummon = {}
mySummon = {}
frSummon = {}

setParameters("種類", "石の種類は何ですか", "マグナ,神石など", mySummon)
setParameters("属性", "属性を入力してください", "火水風土光闇", mySummon)
setParameters("加護", "数値を入力してください", "", mySummon)

setParameters("種類", "石の種類は何ですか", "マグナ,神石,属性など", frSummon)
setParameters("属性", "属性を入力してください", "火水風土光闇", frSummon)
setParameters("加護", "数値を入力してください", "", frSummon)

setParameters("合計ATK", "自分の召喚石の攻撃力合計を入力してください", "", dicSummon)
setParameters("合計HP", "自分の召喚石の体力合計を入力してください", "", dicSummon)
setParameters("HP加護", "召喚石のHP加護(フレ合わせ)を入力してください", "", dicSummon)
setParameters("DA加護", "召喚石のDA加護(フレ合わせ)を入力してください", "", dicSummon)
setParameters("TA加護", "召喚石のTA加護(フレ合わせ)を入力してください", "", dicSummon)

dicSummon["自前"] = mySummon
dicSummon["フレ"] = frSummon

dicWeapon = {}
for i in range(0, 9):
    print("武器IDを入力して下さい")
    res = input()
    if res.isdigit():
        dicWeapon["ID" + str(i)] = res
    else:
        print("test")
        dicWeapon["ID" + str(i)] = 111

data["ジータ"] = dicDjeeta
data["召喚石"] = dicSummon
data["武器"] = dicWeapon

json.dump(data, fileObj, indent=4)
