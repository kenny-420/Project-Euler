from sympy import isprime

def is_pandigital(n):
    digits = list(str(n))
    digits.sort()
    return digits == [str(i) for i in range(1, len(digits)+1)]

for n in range(9999999, 1, -1):
    if is_pandigital(n) and isprime(n):
        print(n)
        break
