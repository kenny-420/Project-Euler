from sympy import primerange

def solve(n):
    t = [1] + [0] * (n)
    for i in primerange(n):
        for j in range(i, n + 1):
            t[j] += t[j - i]
    return t[n]

n = 1
while True:
    n += 1
    if solve(n) > 5000:
        print(n)
        break
