def back(start):
    if len(res) == M:
        print(*res)
        return
    for i in range(start, N):
        # if i not in res:
        res.append(lst[i])
        back(i)
        res.pop()

N, M = map(int, input().split())
lst = sorted([int(x) for x in input().split()])
res = []
back(0)