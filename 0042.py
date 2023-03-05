import requests

words = requests.get("https://projecteuler.net/project/resources/p042_words.txt").text
words = filter(lambda x: x != ',' and x != '', words.split('"'))

triangle_numbers = []
for n in range(1,10000):
    triangle_numbers.append(n*(n+1)//2)

count = 0
for word in words:
    word_value = 0
    for i in word:
        word_value += ord(i) - 64
    if word_value in triangle_numbers:
        count += 1
print(count)
