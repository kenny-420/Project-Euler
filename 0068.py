from itertools import permutations

def sort_z(z):
    while min([i[0] for i in z]) != z[0][0]:
        z = [z[-1]] + z[:-1]
    return z

def max_string(solutions):
    ns = []
    for s in solutions:
        n = ""
        for i in s:
            for j in i:
                n += str(j)
        ns.append(n)
    print(max(ns))

solutions = []
for perm in permutations(range(1, 11)):
    a, b, c, d, e, f, g, h, i, j = perm
    z = [[a,c,e],[b,e,h],[i,h,g],[j,g,d],[f,d,c]]
    if not all([sum(i) == sum(z[0]) for i in z]):
        continue
    z = sort_z(z)
    if z not in solutions:
        solutions.append(z)
        
max_string(solutions)
