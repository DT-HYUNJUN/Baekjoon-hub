from collections import deque
T = int(input())

for _ in range(T):
    N = int(input())
    lst = sorted([int(x) for x in input().split()])
    res = 0
    for i in range(N-2):
        if lst[i+2] - lst[i] > res:
            res = lst[i+2] - lst[i]
    print(res)