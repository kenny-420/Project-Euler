from sympy import isprime
from itertools import combinations
from tqdm import tqdm

def solve(value_family):
    for N in tqdm(range(9999999)):
        if not isprime(N):
            continue

        n = [int(i) for i in str(N)]

        for d in range(1, len(n)):
            for replace in combinations(range(0, len(n)), r=d):
                # check being replaced are initially the same
                if len(set(n[i] for i in replace)) != 1:
                    continue

                count = 0
                n_copy = n.copy()
                for k in range(10):
                    for r in replace:
                        n_copy[r] = k
                    nn = int("".join([str(i) for i in n_copy]))
                    if isprime(nn) and n_copy[0] != 0:
                        count += 1
                
                if count == value_family:
                    return N


print(solve(8))
