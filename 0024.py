from itertools import permutations

for i, p in enumerate(permutations(range(10))):
    if i == 999999:
        print("".join([str(i) for i in p]))
