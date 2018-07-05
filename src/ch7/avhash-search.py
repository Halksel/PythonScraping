from PIL import Image
import numpy as np
import os
import re
from typing import List, Dict, Generator, Iterator, Tuple
from numpy import array

search_dir: str = "./image/101_ObjectCategories"
cache_dir: str = "./image/cache_avhash"

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)


def average_hash(fname: str, size: int = 16) -> array:
    fname2: str = fname[len(search_dir):]
    cache_file: str = cache_dir + "/" + fname2.replace('/', '_') + ".csv"
    if not os.path.exists(cache_file):
        img: Image = Image.open(fname)
        img = img.convert('L')
        img = img.resize((size, size), Image.ANTIALIAS)
        pixels: array = np.array(img.getdata()).reshape(size, size)
        avg: array = pixels.mean()
        px: array = 1 * (pixels > avg)
        np.savetxt(cache_file,px,fmt="%.0f", delimiter=',')
    else:
        px = np.loadtxt(cache_file, delimiter=',')
    return px


def hamming_dist(a: array, b: array) -> int:
    aa: array = a.reshape(1, -1)
    ab: array = b.reshape(1, -1)
    dist = (aa != ab).sum()
    return dist


def enum_all_files(path: str) -> Iterator[str]:
    for root, dirs, files in os.walk(path):
        for f in files:
            fname = os.path.join(root, f)
            if re.search(r'\.(jpg|jpeg|png)$', fname):
                yield fname


def find_image(fname: str, rate: float) -> Iterator[Tuple[float, str]]:
    src = average_hash(fname)
    for fname in enum_all_files(search_dir):
        dst = average_hash(fname)
        diff_r = hamming_dist(src, dst) / 256
        if diff_r < rate:
            yield (diff_r, fname)


srcfile: str = search_dir + "/chair/image_0016.jpg"
html: str = ""
sim = list(find_image(srcfile, 0.25))
sim = sorted(sim, key=lambda x: x[0])

for r, f in sim:
    print(r, ">", f)
    s = '<div style="float:left;"><h3>[差異:' + str(r) + '-' + \
        os.path.basename(f) + ']<h3>' +\
        '<p><a href="' + f + '"><img src="' + f + '" width=400>' +\
        '</a></p></div>'
    html += s

html = """<html><body><h3>元画像</h3><p><img src='{0}' width=400></p>{1}
       </body></html>""".format(srcfile, html)

with open("./avhash-search-output.html", "w", encoding="utf-8") as f2:
    f2.write(html)

print("ok")
