from itertools import permutations
from tqdm import tqdm

primes = [17, 13, 11, 7, 5, 3, 2]

def split_digits(n, a, b):
    return n//(10**b) - (n//(10**(a+b))) * 10**a

def check(n):
    for i, p in enumerate(primes): 
        if split_digits(n, 3, i) % p != 0:
            return False
    return True

sum = 0
pandigitals = [i for i in permutations("0123456789")]
for n in tqdm(pandigitals):
    n = int("".join(n))
    if check(n):
        sum += n
print(sum)
