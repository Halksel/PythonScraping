from janome.tokenizer import Tokenizer
import os
import re
import json
import random
from typing import List, Set, Dict, Tuple, Text, Optional


def make_dic(words: List[str]) -> Dict[str, Dict[str, Dict[str, int]]]:
    tmp: List[str] = ['@']
    dic: Dict[str, Dict[str, Dict[str, int]]] = {}
    for i in words:
        word = i.surface
        if word == "" or word == "\r\n" or word == "\n":
            continue
        tmp.append(word)
        if len(tmp) < 3:
            continue
        if len(tmp) > 3:
            tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == "。":
            tmp = ["@"]
            continue
    return dic


def set_word3(dic: Dict[str, Dict[str, Dict[str, int]]],
              s3: List[str]) -> None:
    w1, w2, w3 = s3
    if w1 not in dic:
        dic[w1] = {}
    if w2 not in dic[w1]:
        dic[w1][w2] = {}
    if w3 not in dic[w1][w2]:
        dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1


def make_sentence(dic):
    ret = []
    if "@" not in dic:
        return "no dic"
    top = dic['@']
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == '。':
            break
        w1, w2 = w2, w3
    return "".join(ret)


def word_choice(sel) -> str:
    keys = sel.keys()
    return random.choice(list(keys))


sjis_file = "kokoro.txt.sjis"
dict_file = "markov-kokoro.json"

if not os.path.exists(dict_file):
    sjis = open(sjis_file, 'rb').read()
    text = sjis.decode('shift_jis')
    text = re.split(r'\-{5,}', text)[2]
    text = re.split(r'底本：', text)[0]
    text = text.strip()
    text = text.replace('|', '')
    text = re.sub(r'《.+?》', '', text)
    text = re.sub(r'［＃.+?］', '', text)
    t = Tokenizer(text)
    words = t.tokenize(text)
    dic = make_dic(words)
    json.dump(dic,open(dict_file,'w',encoding='utf-8'))
else:
    dic = json.load(open(dict_file, 'w'))

for i in range(3):
    s = make_sentence(dic)
    print(s)
    print('---')
