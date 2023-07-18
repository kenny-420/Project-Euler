from sympy.abc import x, y, t
from sympy.solvers.diophantine.diophantine import diop_quadratic
from sympy import simplify
from tqdm import tqdm

max_d = 0
max_x = 0

for d in tqdm(range(2, 1000)):
    solve = diop_quadratic(x**2 - d * y**2 - 1, t)

    for i in solve:
        solution = simplify(i.subs({t: 0}))
        xx = solution[0]
        if xx > max_x:
            max_x = xx
            max_d = d

print(max_d)
