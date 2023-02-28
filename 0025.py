fib = [1,1]
i = 1
while True:
    i += 1
    fib.append(fib[-1] + fib[-2])
    if len(str(fib[i])) >= 1000:
        print(i+1)
        break
