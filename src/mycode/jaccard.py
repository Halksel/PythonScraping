from numpy import random
from typing import List, Dict, Tuple, TypeVar, Set, functools
from collections import Counter, Mapping
import hashlib

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


def create_hash(f, shift):
    def func(x):
        return f((str(x) + shift).encode())

    return func


a: Set[int] = set(random.randint(0, 100, 100))
b: Set[int] = set(random.randint(50, 150, 100))

print(a)
print(b)

f1 = create_hash(lambda x: hashlib.md5(str(x).encode()).hexdigest(), '')
f2 = create_hash(lambda x: hashlib.md5(str(x).encode()).hexdigest(), 'aa')
f3 = create_hash(lambda x: hashlib.md5(str(x).encode()).hexdigest(), 'aaa')
f4 = create_hash(lambda x: hashlib.sha256(str(x).encode()).hexdigest(), '')
f5 = create_hash(lambda x: hashlib.sha256(str(x).encode()).hexdigest(), 'aa')
f6 = create_hash(lambda x: hashlib.sha256(str(x).encode()).hexdigest(), 'aaa')

hashs = [f1, f2, f3, f4, f5, f6]

print(jaccard(a, b))
print(min_hash_sketch(a, b, hashs))
