from tqdm import tqdm

total_sum = 0
for n in tqdm(range(2, 1000000)):
    if sum(int(i)**5 for i in str(n)) == n:
        total_sum += n

print(total_sum)
