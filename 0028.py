i = 1
sum = 1
for j in range(2, 1001, 2):
    for _ in range(4):
        i += j
        sum += i
print(sum)
