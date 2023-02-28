from math import isqrt
from tqdm import tqdm

def d(n):
    sum = 1
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            if i**2 == n:
                sum += i
            else:
                sum += i + n//i
    return sum

def is_abundant(n):
    return d(n) > n

A = []
N = 20162

for i in range(1, N):
    if is_abundant(i):
        A.append(i)

possible = set() # like a list but will remove duplicates automatically
for a in tqdm(A):
    for b in A:
        if a+b < N:
            possible.add(a + b)
        
print(sum([p for p in range(N) if p not in possible]))
