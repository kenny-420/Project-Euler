from gmpy2 import iroot
from tqdm import tqdm

count = 0

for i in tqdm(range(2, 10001)):
    if not iroot(i, 2)[1]:
        K.<x> = QuadraticField(i)
        period = continued_fraction(x).period()
        if len(period) % 2 == 1:
            count += 1

print(count)
