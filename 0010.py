import sympy

sum = 2
p = 3
while True:
    if sympy.isprime(p):
        sum += p

    if p >= 2000000 - 1:
        break
    p += 2
print(sum)
