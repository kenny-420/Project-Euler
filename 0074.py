from math import factorial
from tqdm import tqdm

def f(n):
    return sum([factorial(int(i)) for i in str(n)])

def count(n):
    a = [n]
    while True:
        next = f(a[-1])
        if next in a:
            break
        else:
            a.append(f(a[-1]))
    return len(a)

s = 0
for n in tqdm(range(1000000)):
    if count(n) == 60:
        s += 1
print(s)
