a = 0
b = 2
c = 3
sum = 2

while c < 4000000:
    a = b
    b = c
    c = a + b
    if c % 2 == 0:
        sum += c

print(sum)

