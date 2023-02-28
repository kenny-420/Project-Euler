import itertools

TRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def calculate_route_sum(triangle, path):
    route_sum = triangle[0][0]
    position = 0

    for (i, p) in enumerate(path):
        position += p
        route_sum += triangle[i+1][position]
    return route_sum

lines = TRIANGLE.strip().split("\n")
size = len(lines)
triangle = [[] for _ in range(size)]

for (i, line) in enumerate(lines):
    for n in line.split(" "):
        triangle[i].append(int(n))

# now bruteforce all the routes
# adding 0 to the current position will go left
# adding 1 to the current position will go right
# there are 14 choices to make to get to the bottom

max_route_sum = 0
for path in itertools.product([0, 1], repeat=size-1):
    route_sum = calculate_route_sum(triangle, path)
    if route_sum > max_route_sum:
        max_route_sum = route_sum

print(max_route_sum)
