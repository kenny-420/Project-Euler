from sympy import factorint

def distinct_factors(n):
    return len(factorint(n))

count = 0
consecutive = 4
for n in range(1, 999999):
    if distinct_factors(n) == consecutive:
        count += 1
    else:
        count = 0
    if count == consecutive:
        print(n - consecutive + 1)
        break
