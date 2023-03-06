from itertools import permutations, combinations, combinations_with_replacement
from Crypto.Util.number import isPrime

for i in combinations_with_replacement("0123456789", 4):
    primes = []
    for j in permutations("".join(i)):
        n = int("".join(j))
        if isPrime(n) and n > 1000 and n not in primes:
            primes.append(n)

    for k in combinations(primes, 3):
        k = list(k)
        k.sort()
        a,b,c = k
        if c-b == b-a and a != c and a != 1487:
            print(f"{a}{b}{c}")
