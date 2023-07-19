from tqdm import tqdm

max_n = 0
max_ratio = 0
for n in tqdm(range(1, 1000000)):
    ratio = n / euler_phi(n)
    if ratio > max_ratio:
        max_ratio = ratio
        max_n = n
print(max_n)
