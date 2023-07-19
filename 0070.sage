from tqdm import tqdm

min_n = 0
min_ratio = 999999999999999999999999999999999
for n in tqdm(range(2, 10000000)):
    phi = euler_phi(n)
    if sorted(str(n)) != sorted(str(phi)):
        continue
    ratio = n / phi
    if ratio < min_ratio:
        min_ratio = ratio
        min_n = n
print(min_n)
