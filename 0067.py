import requests


TRIANGLE = requests.get("https://projecteuler.net/resources/documents/0067_triangle.txt").text
lines = TRIANGLE.strip().split("\n")
size = len(lines)
t = [[] for _ in range(size)]

for (i, line) in enumerate(lines):
    for n in line.split(" "):
        t[i].append(int(n))

for i in range(len(t)-2, -1, -1):
    for j in range(i+1):
      t[i][j] += max(t[i+1][j], t[i+1][j+1])

print(t[0][0])
