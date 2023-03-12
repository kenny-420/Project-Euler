def get_min(n):
    for i in range(9999):
        nn = "".join(sorted(str(i**3)))
        if n == nn:
            return i**3

N = 5
dict = {}
for i in range(9999):
    n = "".join(sorted(str(i**3)))
    if dict.get(n) is None:
        dict[n] = 1
    else:
        dict[n] += 1
        if dict[n] == N:
            print(get_min(n))
            break
