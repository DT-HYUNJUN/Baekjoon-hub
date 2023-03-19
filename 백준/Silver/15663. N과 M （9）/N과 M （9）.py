def back():
    if len(tmp) == M:
        res = (tuple([lst[x] for x in tmp]))
        dic[res] = dic.get(res, 0)+1
        return
    for i in range(N):
        if i not in tmp:
            tmp.append(i)
            back()
            tmp.pop()

N, M = map(int, input().split())
lst = sorted([int(x) for x in input().split()])
tmp = []
res = ()
dic = {}
back()
for k, v in dic.items():
    print(*k)