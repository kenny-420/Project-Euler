from math import isqrt

def count_divisors(n):
    count = 0
    for i in range(1, isqrt(n)):
        if n % i == 0:
            if i*i == n:
                count += 1
            else:
                count += 2
    return count

n = 1
i = 2
while True:
    if count_divisors(n) > 500:
        break
    n += i
    i += 1
print(n)
