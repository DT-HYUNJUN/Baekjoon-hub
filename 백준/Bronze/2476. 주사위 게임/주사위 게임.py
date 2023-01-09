T = int(input())
sum = []
for _ in range(T):
    DICE = list(map(int, input().split()))
    DICE.sort()
    if DICE[0] == DICE[2]:
        sum.append(10000 + DICE[0]*1000)
    elif DICE[0] == DICE[1] or DICE[1] == DICE[2]:
        sum.append(1000 + DICE[1]*100)
    else:
        sum.append(DICE[2]*100)
print(max(sum))        