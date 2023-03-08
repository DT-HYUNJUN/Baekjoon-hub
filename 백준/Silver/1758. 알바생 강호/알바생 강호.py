import sys
N = int(input())
tips = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)], reverse=True)
total = 0
for index, tip in enumerate(tips):
    tip_take = tip - (index + 1 - 1)
    if tip_take > 0:
        total += tip_take
print(total)