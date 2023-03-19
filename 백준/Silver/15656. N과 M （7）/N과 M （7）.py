def back():
    if len(res) == M:
        print(*res)
        return
    for i in range(N):
        # if lst[i] not in res:
        res.append(lst[i])
        back()
        res.pop()

N, M = map(int, input().split())
lst = sorted([int(x) for x in input().split()])
res = []
back()