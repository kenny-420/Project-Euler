from tqdm import tqdm

pent = []
hex = []

for n in range(1, 100000):
    pent.append(n*(3*n-1)//2)
    hex.append(n*(2*n-1))

def solve():
    for p in tqdm(pent):
        if p in hex and p > 40755:
            return p

print(solve())
