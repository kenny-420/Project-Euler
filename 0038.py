from tqdm import tqdm

def concat_product(x, n):
    s = ""
    for i in range(1, n+1):
        s += str(i*x)

    # check pandigital
    digits = list(s)
    digits.sort()
    if "".join(digits) != "123456789":
        return 0

    return int(s)
    
max = 0
for x in tqdm(range(1, 100000)): 
    for n in range(1, 10):
        p = concat_product(x, n)
        if p > max:
            max = p
print(max)
