from Crypto.Util.number import isPrime, sieve_base

max_s = 0
max_len = 0
for i in range(1000):
    for j in range(i):
        l = i-j 
        s = sum(sieve_base[j:i])
        if s > 1000000:
            break
        if  l > max_len and isPrime(s):
            max_len = l 
            max_s = s
print(max_s)
