from PIL import Image
import numpy as np
from typing import List, Dict
from numpy import array


def average_hash(fname: str, size: int = 16) -> array:
    img: Image = Image.open(fname)
    img = img.convert('L')
    img = img.resize((size, size), Image.ANTIALIAS)
    pixel_data: List[int] = img.getdata()
    pixels: array = np.array(pixel_data)
    pixels = pixels.reshape((size, size))
    avg: array = pixels.mean()
    diff: array = 1 * (pixels > avg)
    return diff


def np2hash(n: array) -> str:
    bhash = []
    for nl in n.tolist():
        sl: List[str] = [str(i) for i in nl]
        s2 = "".join(sl)
        i: int = int(s2, 2)
        bhash.append("%04x" % i)
    return "".join(bhash)


ahash = average_hash('tower.jpg')
print(ahash)
print(np2hash(ahash))
