def get_frac(iters):
    numerator = 1
    denominator = 2
    for _ in range(iters-1):
        numerator += 2*denominator
        numerator, denominator = denominator, numerator
    numerator += denominator
    return numerator, denominator


count = 0
for i in range(1, 1000):
    numerator, denominator = get_frac(i)
    if len(str(numerator)) > len(str(denominator)):
        count += 1
print(count)
