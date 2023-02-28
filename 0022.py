import requests

score = 0
file = requests.get("https://projecteuler.net/project/resources/p022_names.txt").text
names = []
for name in file.split('"'):
    if name == ',' or name == '':
        continue
    names.append(name)

names.sort()
for i, name in enumerate(names):
    score += (i+1) * sum(ord(i)-64 for i in name)
print(score)


