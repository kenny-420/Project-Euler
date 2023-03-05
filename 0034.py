from math import factorial

answer = 0
for n in range(3, 1000000):
    if sum([factorial(int(i)) for i in str(n)]) == n:
        answer += n
print(answer)
