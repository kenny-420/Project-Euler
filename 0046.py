from sympy import isprime
from math import isqrt
from tqdm import tqdm

def test(n):
    for p in range(1, n):
        if isprime(p):
            s = isqrt((n-p)//2)
            if p + 2*s**2 == n:
                return True
    return False

def solve():
    for n in tqdm(range(3, 10000, 2)):
        if not isprime(n):
            if not test(n):
                return n

print(solve())
