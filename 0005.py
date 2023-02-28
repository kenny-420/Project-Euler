n = 0
while True:
    n += 20 * 3 * 7 * 11 * 13 * 17 * 19
    evenly_divisible = True 
    for i in range(11, 21):
        if n % i != 0:
            evenly_divisible = False
            break
    if evenly_divisible:
        print(n)
        break
