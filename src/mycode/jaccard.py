from numpy import random
from typing import List, Dict, Tuple, TypeVar, Set, functools
from collections import Counter, Mapping
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


def create_hash(t):
    f = t[0]
    shift = t[1]

    def func(x):
        return f((str(x) + shift).encode()).hexdigest()

    return func


a: Set[int] = set(random.randint(0, 100, 100))
b: Set[int] = set(random.randint(50, 150, 100))

print(a)
print(b)

fs = [hashlib.md5, hashlib.sha256, hashlib.sha224]
shifts = ['', 'a', 'aa', 'aaa']
hashs = list(map(create_hash, itertools.product(fs, shifts)))

print(jaccard(a, b))
print(min_hash_sketch(a, b, hashs))
