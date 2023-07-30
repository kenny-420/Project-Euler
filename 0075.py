from math import gcd, isqrt
from tqdm import tqdm

limit = 1_500_000
perimiter_map = {}
count = 0

for m in tqdm(range(isqrt(limit//2) + 1)):
    for n in range(1, m):
        if (m+n) % 2 == 1 and gcd(m, n) == 1:
            x = m**2 + m**2 + 2*m*n
            k = 0
            while True:
                k += 1
                p = k*x
                if p > limit:
                    break
                else:
                    num_count = perimiter_map.get(p) or 0
                    perimiter_map[p] = num_count + 1
                    if num_count == 0:
                        count += 1
                    elif num_count == 1:
                        count -= 1
print(count)
