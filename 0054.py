from collections import Counter
import requests

file = requests.get("https://projecteuler.net/project/resources/p054_poker.txt").text

def canonical(hand):
    flush = len(set(suit for _, suit in hand)) == 1
    ranks = sorted('--23456789TJQKA'.find(rank) for rank, _ in hand)
    if ranks == [2, 3, 4, 5, 14]: # ace-low straight
        ranks = [1, 2, 3, 4, 5]
    straight = ranks == list(range(ranks[0], ranks[0] + 5))
    count = Counter(ranks)
    counts = sorted(count.values())
    distinct_ranks = sorted(count, reverse=True, key=lambda v:(count[v], v))
    if flush and straight:       q = 9 #straight_flush
    elif counts == [1, 4]:       q = 8 #four
    elif counts == [2, 3]:       q = 7 #full_house
    elif flush:                  q = 6 #flush
    elif straight:               q = 5 #straight
    elif counts == [1, 1, 3]:    q = 4 #three
    elif counts == [1, 2, 2]:    q = 3 #two_pairs
    elif counts == [1, 1, 1, 2]: q = 2 #pair
    else:                        q = 1 #high_card
    return q, distinct_ranks


count = 0
for line in file.splitlines():
    player1 = line.split()[:5]
    player2 = line.split()[5:]
    if canonical(player1) > canonical(player2):
        count += 1
print(count)
