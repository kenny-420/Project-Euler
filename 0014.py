import tqdm

def collatz(start):
    count = 1
    n = start
    while True:
        count += 1
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return count

max = 0
max_start = 0
for i in tqdm.tqdm(range(1, 1000000)):
    if collatz(i) > max:
        max = collatz(i)
        max_start = i
print(max_start)

