from collections import defaultdict
from random import shuffle
from random import choice

games = "".split("\n")
shuffle(games)

comparisons = []
wins = defaultdict(int)
plays = defaultdict(int)

for first in games:
    second = choice([q for q in games if q != first and (first, q) not in [(x1, x2) for x1, x2, x3 in comparisons]])
    ans = input(first + " / " + second + ": ")
    if ans == "1":
        wins[first]+=1
        comparisons.append((first, second, first))
        comparisons.append((second, first, first))
    else:
        wins[second]+=1
        comparisons.append((first, second, second))
        comparisons.append((second, first, second))

    plays[first] += 1
    plays[second] += 1

games.sort(key=lambda x: wins[x] / plays[x], reverse=True)
while True:
    retry=False
    for i in range(len(games) - 1):
        if wins[games[i]]/plays[games[i]] > wins[games[i + 1]]/plays[games[i + 1]] or \
                (games[i], games[i + 1], games[i]) in comparisons:
            continue
        elif (games[i], games[i + 1], games[i + 1]) in comparisons:
            games[i], games[i + 1] = games[i + 1], games[i]
            retry=True
            break

        else:
            break
    else:
        break

    if retry:
        continue

    ans = input(games[i] + " / " + games[i + 1] + ": ")
    if ans == "1":
        wins[games[i]]+=1
        comparisons.append((games[i], games[i + 1], games[i]))
        comparisons.append((games[i + 1], games[i], games[i]))
    else:
        wins[games[i + 1]]+=1
        comparisons.append((games[i], games[i + 1], games[i + 1]))
        comparisons.append((games[i + 1], games[i], games[i + 1]))

    plays[games[i]] += 1
    plays[games[i + 1]] += 1
    games.sort(key=lambda x: wins[x] / plays[x], reverse=True)

print(games[0])
