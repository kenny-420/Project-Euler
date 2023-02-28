import sympy

count = 1
p = 3
while True:
    if sympy.isprime(p):
        count += 1
    if count == 10001:
        print(p)
        break
    p += 2
