from itertools import product
from math import gcd

numerator = 1
denominator = 1

for (a,b,c,d) in product(range(1,10), repeat=4):
    x = 10*a + b
    y = 10*c + d

    if d == 0 or a == b or x > y:
        continue

    if x/y == a/d and b == c:
        #print(f"{a}{b}/{c}{d}")
        numerator *= x
        denominator *= y

print(denominator // gcd(numerator, denominator))
