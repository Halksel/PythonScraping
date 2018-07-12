from numpy import random
from typing import List, Dict, Tuple, TypeVar, Set, functools
from collections import Counter, Mapping
from math import log
import hashlib
import itertools

T = TypeVar('T')


def jaccard(a: Set[T], b: Set[T]) -> float:
    union_ab = a.union(b)
    intersection_ab = a.intersection(b)
    return len(intersection_ab) / len(union_ab)


def min_hash_sketch(a: Set[T], b: Set[T], hashs) -> float:
    count: int = 0
    k = len(hashs)
    print("calculate " + str(k) + " min-hash")
    for f in hashs:
        fa = min(map(lambda x: f(x), a))
        fb = min(map(lambda x: f(x), b))
        if fa == fb:
            count += 1

    return count / k


def odd_sketch(a: Set[T], hashs, n) -> List[int]:
    s: List[int] = [0 for i in range(n)]
    hashFunction = create_hash((hashlib.sha256, 'afde'))
    S = []
    for f in hashs:
        S.append(min(map(lambda x: f(x), a)))
    for x in S:
        hx = hashFunction(x)
        s[hx % n] = ~s[hx % n]
    return s


def odd_sketch_hash(a: Set[T], b: Set[T], hashs, n) -> float:
    k: int = len(hashs)
    oa = odd_sketch(a, hashs, n)
    ob = odd_sketch(b, hashs, n)
    diff: int = 0
    for idx, v in enumerate(oa):
        diff += oa[idx] ^ ob[idx]
    return (1 + n / (4 * k) * log(1 - 2 * diff / n))


def create_hash(t):
    f = t[0]
    shift = t[1]

    def func(x):
        return int(f((str(x) + shift).encode()).hexdigest(), 16)

    return func


# a: Set[int] = set(random.randint(0, 100, 100))
# b: Set[int] = set(random.randint(50, 150, 100))
a = set(["さかい", "水炊き", "焼肉", "ゆうじ", "ハツ", "鶏ガラ", "登録", "雑炊"])
b = set(["さかい", "水炊き", "焼肉", "ゆうじ", "ハツ", "鶏ガラ", "登録", "テール"])
c = set(["さかい", "水炊き", "焼肉", "ゆうじ", "ハツ", "鶏ガラ", "登録", "テール", "雑炊"])

print(a)
print(b)

fs = [hashlib.md5, hashlib.sha256, hashlib.sha224]
shifts = ['', 'a', 'aa', 'aaa', 'fauif', 'sfhs', 'sghei', 'dfiuew', 'ddf', 'fefef', 's', 'sf', 'hg']
hashs = list(map(create_hash, itertools.product(fs, shifts)))
hashFunction = create_hash((hashlib.sha256, 'afde'))

print(jaccard(a, b))
print(min_hash_sketch(a, b, hashs))
print(odd_sketch_hash(a, b, hashs, 1007))
