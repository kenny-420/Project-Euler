s = ""
for i in range(1, 999999):
    s += str(i)

product = 1;
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    product *= int(s[i-1])
print(product)
