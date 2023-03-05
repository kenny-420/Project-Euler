from sympy import isprime
from tqdm import tqdm

def trunk_left(n):
    n = str(n)
    result = []
    while len(n) > 1:
        n = n[1:]
        result.append(int(n))
    return result

def trunk_right(n):
    n = str(n)
    result = []
    while len(n) > 1:
        n = n[:-1]
        result.append(int(n))
    return result

sum = 0
for p in tqdm(range(10, 1000000)):
    if not isprime(p):
        continue
    all_prime = True
    for i in trunk_right(p):
        if not isprime(i):
            all_prime = False
    for i in trunk_left(p):
        if not isprime(i):
            all_prime = False
    if all_prime:
        sum += p
print(sum)

