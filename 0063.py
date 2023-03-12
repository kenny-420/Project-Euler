from tqdm import tqdm

lst = []
for i in tqdm(range(99)):
    for l in range(99):
        n = i**l
        if len(str(n)) == l:
            lst.append(n)

print(len(lst) - 1) #exclude 0
