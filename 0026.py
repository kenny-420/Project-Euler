def cycle_len(n):
    rest = 1
    for _ in range(n):
        rest = (rest*10) % n;
    r0 = rest
    len = 0
    while True:
        rest = (rest*10) % n
        len += 1
        if rest == r0:
            break
    return len

maxlen = 0
maxn = 0
for n in range(2, 1000):
    len = cycle_len(n)
    if len>maxlen:
        maxn = n
        maxlen = len
print(maxn)
