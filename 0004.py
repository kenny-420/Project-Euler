def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest = 0
for i in range(1000):
    for j in range(1000):
        n = i * j
        if n > largest and is_palindrome(n):
            largest = n

print(largest)
