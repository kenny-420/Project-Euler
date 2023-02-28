from math import isqrt

def d(n):
    sum = 1
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            if i**2 == n:
                sum += i
            else:
                sum += i + n//i
    return sum

def is_amicable(n):
    return d(d(n)) == n and d(n) != n

sum = 0;
for i in range(2, 10000):
    if is_amicable(i):
        sum += i
print(sum)
