from sympy import isprime
from tqdm import tqdm

def circle(n):
    result = []
    n = str(n)
    for _ in range(1, len(n)+1):
        n = n[-1] + n[:-1]
        result.append(int(n))
    return result

count = 0
for x in tqdm(range(1, 1000000)):
    all_prime = True
    for p in circle(x):
        if not isprime(p):
            all_prime = False
    if all_prime:
        count += 1
print(count)
