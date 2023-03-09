max = 0
for a in range(100):
    for b in range(100):
        n = a**b
        digit_sum = sum(int(i) for i in str(n))
        if digit_sum > max:
            max = digit_sum
print(max)
