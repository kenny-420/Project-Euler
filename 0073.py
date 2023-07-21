from tqdm import tqdm

x = []
for a in tqdm(range(10001)):
    for b in range(a+1, 10001):
        f = a/b
        if 1/3 < f < 1/2:
            x.append(f)
print(len(set(x)))
