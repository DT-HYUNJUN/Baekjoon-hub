T = int(input())
for _ in range(T):
    lst = sorted([int(x) for x in input().split()])[1:-1]
    print('KIN' if max(lst) - min(lst) >= 4 else sum(lst))