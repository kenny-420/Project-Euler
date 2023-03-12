# generate sequences
seqs = [    
    [n*(n+1)//2 for n in range(200) if 1000 <= n*(n+1)//2 < 10000],
    [n*n for n in range(200) if 1000 <= n*n < 10000],
    [n*(3*n-1)//2 for n in range(200) if 1000 <= n*(3*n-1)//2 < 10000],
    [n*(2*n-1) for n in range(200) if 1000 <= n*(2*n-1) < 10000],
    [n*(5*n-3)//2 for n in range(200) if 1000 <= n*(5*n-3)//2 < 10000],
    [n*(3*n-2) for n in range(200) if 1000 <= n*(3*n-2) < 10000]
]

# create a dictionary to store sequences by their first two digits
seq_dict = [{} for _ in range(len(seqs))]
for i in range(len(seqs)):
    for n in seqs[i]:
        key = str(n)[:2]
        if key not in seq_dict[i]:
            seq_dict[i][key] = {n}
        else:
            seq_dict[i][key].add(n)

# find solutions
for n in seqs[-1]:
    stack = [(n, set(range(len(seqs)-1)), n)]
    while stack:
        current, remaining, acc = stack.pop()
        if not remaining and str(current)[2:] == str(n)[:2]:
            print(acc)
        else:
            for i in remaining:
                if str(current)[2:] in seq_dict[i]:
                    for r in seq_dict[i][str(current)[2:]]:
                        stack.append((r, remaining - {i}, acc + r))
