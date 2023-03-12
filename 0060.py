from sympy import isprime
from tqdm import tqdm


def prime_concat(a, b):
    return isprime(int(str(a) + str(b))) and isprime(int(str(b) + str(a)))

def solve(lst, N, solution):
    for a in lst:
        templist = []
        for b in lst:
            if b > a and prime_concat(a[-1], b[-1]):
                templist.append(a.copy() + [b[-1]])
                if len(templist[-1]) == N:
                    solution.append(sum(templist[-1]))
        solve(templist, N, solution)
    return solution

def main():
    MAX = 10000
    primes = [i for i in range(3, MAX, 2) if isprime(i)]
    sums = []

    for p1 in tqdm(primes):
        lst = []
        for p2 in primes:
            if p2 > p1 and prime_concat(p1, p2):
                lst.append([p1, p2])
        
        s = solve(lst, 5, [])
        if s != []:
            sums.append(min(s))
    print(min(sums))

main()
