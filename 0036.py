def is_palindrome(s):
    return s == s[::-1]

def check(n):
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])

print(sum(n if check(n) else 0 for n in range(1, 1000000)))
