from sympy import isprime

prime_count = 0
n = 1
x = 1

while True:
    n += 2
    for _ in range(4):
        x += 2*(n//2)
        if isprime(x):
            prime_count += 1

    ratio = prime_count / (2*n-1)
    if ratio < 0.1:
        print(n)
        break
