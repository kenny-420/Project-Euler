n = 20
while True:
    evenly_divisible = True 
    for i in range(11, 21):
        if n % i != 0:
            evenly_divisible = False
            break
    if evenly_divisible:
        print(n)
        break
    n += 20
