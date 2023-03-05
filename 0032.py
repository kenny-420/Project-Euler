from itertools import permutations

def is_pandigital(n):
    digits = list(str(n))
    digits.sort()
    return digits == [str(i) for i in range(1, len(digits)+1)]

products = []
for n in permutations(range(1,10)):
    n = int("".join([str(i) for i in n]))
    if is_pandigital(n):
        for x in range(1, 9):
            for y in range(x+1, 9):
                n = str(n)
                multiplicand = int(n[:x])
                multiplier = int(n[x:y])
                product = int(n[y:])
                if multiplicand * multiplier == product:
                    products.append(product)
print(sum(set(products)))
