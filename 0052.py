from tqdm import tqdm

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def check(x):
    for k in range(2, 7):
        if not is_permutation(x, k*x):
            return False
    return True

for x in tqdm(range(1, 999999)):
    if check(x):
        print(x)
        break
