from tqdm import tqdm

def S(n):
    return sum([euler_phi(i) for i in tqdm(range(2, n+1))])

print(S(1000000))
