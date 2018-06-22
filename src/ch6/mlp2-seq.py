import os
import glob
import json

root_dir = './newstext'
dic_file = root_dir + '/word-dic.json'
data_file = root_dir + '/data.json'
data_file_min = root_dir + '/data-mini.json'

# 語句を区切ってIDに変換する---(*1)
word_dic = {"_MAX": 0}


def text_to_ids(text):
    text = text.strip()
    words = text.split(' ')
    result = []
    for n in words:
        n = n.strip()
        if n == '':
            continue
        if n not in word_dic:
            wid = word_dic[n] = word_dic['_MAX']
            word_dic['_MAX'] += 1
            print(wid, n)
        else:
            wid = word_dic[n]
        result.append(wid)
    return result


# ファイルを読んで固定長シーケンスを返す---(*2)
def file_to_ids(fname):
    with open(fname, 'r') as f:
        text = f.read()
        return text_to_ids(text)


# 辞書に全部の単語を登録する --- (※3)
def register_dic():
    files = glob.glob(root_dir + '/*/*.wakati', recursive=True)
    for i in files:
        file_to_ids(i)


# ファイル内の単語を数える --- (※4)
def count_file_freq(fname):
    cnt = [0 for n in range(word_dic['_MAX'])]
    with open(fname, 'r') as f:
        text = f.read().strip()
        ids = text_to_ids(text)
        print(str(max(ids)) + ',' + str(word_dic['_MAX']))
        for wid in ids:
            try:
                cnt[wid] += 1
            except IndexError as e:
                wid = 0

    return cnt


# ジャンルごとにファイルを読み込む --- (※5)
def count_freq(limit=0):
    X = []
    Y = []
    cat_names = []
    for cat in os.listdir(root_dir):
        cat_dir = root_dir + '/' + cat
        if not os.path.isdir(cat_dir):
            continue
        cat_idx = len(cat_names)
        cat_names.append(cat)
        files = glob.glob(cat_dir + '/*.wakati')
        i = 0
        for path in files:
            print(path)
            cnt = count_file_freq(path)
            X.append(cnt)
            Y.append(cat_idx)
            if limit > 0:
                if i > limit:
                    break
                i += 1
    return X, Y


if os.path.exists(dic_file):
    word_dic = json.load(open(dic_file))
else:
    register_dic()
    json.dump(word_dic, open(dic_file, 'w'))

X, Y = count_freq(20)
json.dump({'X': X, 'Y': Y}, open(data_file_min, 'w'))
X, Y = count_freq()
json.dump({'X': X, 'Y': Y}, open(data_file, 'w'))

print('ok')
