def solve(n):
    t = [1] + [0] * (n)
    for i in range(1, n):
        for j in range(i, n + 1):
            t[j] += t[j - i]
    return t[n]

print(solve(100))
