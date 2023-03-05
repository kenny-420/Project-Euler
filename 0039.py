from math import isqrt
from tqdm import tqdm

def count_solutions(p):
    count = 0
    for a in range(1, p//4):
        for b in range(a+1, (p-a)//2):
            c = isqrt(a**2 + b**2)
            if a+b+c == p and a**2 + b**2 == c**2:
                count += 1
    return count

max = 0
max_p = 0
for p in tqdm(range(1, 1000)):
    s = count_solutions(p)
    if s > max:
        max = s
        max_p = p
print(max_p)
