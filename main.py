L = """7 Wonders
7 Wonders Duels
Activity
Aeon's End
Battleships
Black Dog
Bluff
Bohnanza
Catan
Chess
Clue
Codenames
Codenames Duet
Codenames Pictures
Connect 4
Exploding Kittens
Fox in the Forest
Guess Who?
Jaipur
Klattschen
Ligretto
Ligretto Dice
Ligretto Twist
Lost Cities
Mensch ärgere Dich nicht
Mister X - Hunt through London
Monopoly
Munchkin
Old Maid
Pandemic
Phase 10
Pictures
Poker
Pucket
Risk
Rommé
Schach
Scotland Yard
Scrabble
Skip-Bo
The Crew
The Mind
UNO
Villainous
Werewolf
Who Wants to Be a Millionaire
Wingspan
Wizard"""

L = L.split("\n")
comparisons = []
wins = {i : 0 for i in L}
plays = {i : 0 for i in L}

import random
random.shuffle(L)

for a in L:
    b = random.choice([q for q in L if q != a and (a,q) not in [(x1,x2) for x1,x2,x3 in comparisons]])
    ans = input(a + " / " + b + ": ")
    if ans == "1":
        wins[a]+=1
        comparisons.append((a,b,a))
        comparisons.append((b,a,a))
    else:
        wins[b]+=1
        comparisons.append((a,b,b))
        comparisons.append((b,a,b))

    plays[a] += 1
    plays[b] += 1

L.sort(key=lambda x: wins[x]/plays[x], reverse=True)
while True:
    retry=False
    for i in range(len(L)-1):
        if wins[L[i]]/plays[L[i]] > wins[L[i+1]]/plays[L[i+1]] or \
                (L[i], L[i+1], L[i]) in comparisons:
            continue
        elif (L[i], L[i+1], L[i+1]) in comparisons:
            L[i], L[i+1] = L[i+1], L[i]
            retry=True
            break

        else:
            break
    else:
        break

    if retry:
        continue

    ans = input(L[i] + " / " + L[i+1] + ": ")
    if ans == "1":
        wins[L[i]]+=1
        comparisons.append((L[i],L[i+1],L[i]))
        comparisons.append((L[i+1],L[i],L[i]))
    else:
        wins[L[i+1]]+=1
        comparisons.append((L[i],L[i+1],L[i+1]))
        comparisons.append((L[i+1],L[i],L[i+1]))

    plays[L[i]] += 1
    plays[L[i+1]] += 1
    L.sort(key=lambda x: wins[x]/plays[x], reverse=True)

print(L)

    
    
    
