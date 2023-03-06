from math import sqrt
from tqdm import tqdm

def pent(x):
    return x*(3*x-1)//2

def is_pent(x):
    f = (sqrt(24*x+1)+1)/6
    return f - int(f) == 0

def solve():
    n = 3000
    for i in tqdm(range(1, n)):
        for j in range(i, n):
            diff = pent(j) - pent(i)
            sum = pent(j) + pent(i)
            if is_pent(sum) and is_pent(diff):
                return diff

print(solve())
