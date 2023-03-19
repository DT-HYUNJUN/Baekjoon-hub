def back(start):
    if len(res) == M:
        print(*res)
        return
    for i in range(start, N):
        if lst[i] not in res:
            res.append(lst[i])
            back(i+1)
            res.pop()

N, M = map(int, input().split())
lst = sorted([int(x) for x in input().split()])
res = []
back(0)