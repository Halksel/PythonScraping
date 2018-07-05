from PIL import Image
import pickle
import os
import numpy as np
import random
import math
from typing import List, Dict, Tuple

imgPath: str = '../datas/img/weapons'
with open("../datas/pickles/weapon.pickle", 'rb') as f:
    datas = pickle.load(f)

category = ["火", "水", "風", "土", "光", "闇", ""]
nb_class = len(category)
image_size = 64

X = []
Y = []


def add_sample(cat: int, fname: str, is_train: bool) -> None:
    img: Image = Image.open(fname).convert("RGB")
    img = img.resize((image_size, image_size))
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)
    if not is_train:
        return
    for ang in range(-20, 20, 5):
        img2 = img.rotate(ang)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)
        img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)


def make_sample(files: List[str], is_train: bool) -> tuple:
    global X, Y
    X = []; Y = []
    for k in files:
        add_sample(category.index(datas[k][0]), imgPath + "/" + k + ".png", is_train)
    return np.array(X), np.array(Y)

names = list(datas.keys())
random.shuffle(names)
th = math.floor(len(names) * 0.6)
train = []
test = []
for i, k in enumerate(names):
    if i < th:
        train.append(k)
    else:
        test.append(k)

X_train, Y_train = make_sample(train, True)
X_test, Y_test = make_sample(test, False)
xy = (X_train, Y_train, X_test, Y_test)
np.save("../datas/pickles/weapon.npy", xy)
print(Y_train)
