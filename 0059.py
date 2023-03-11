from string import ascii_lowercase
from itertools import product
from pwn import xor
import requests

file = requests.get("https://projecteuler.net/project/resources/p059_cipher.txt").text
enc = bytes([int(i) for i in file.split(',')])

for p in product(ascii_lowercase, repeat=3):
    key = "".join(p).encode()
    decrypted = xor(enc, key)
    if b" the " in decrypted:
        #print(decrypted.decode())
        print(sum([i for i in decrypted]))
        break
