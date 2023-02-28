from sympy import isprime
from tqdm import tqdm

s = 1000
counts = {}
for a in tqdm(range(-s, s)):
    for b in range(-s, s):
        n = 0
        count = 0
        while True:
            x = n**2 + a*n + b
            if x  <1 or not isprime(x):
                break
            count += 1
            n += 1
        counts[count] = a*b
print(counts[max(counts)])
