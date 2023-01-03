N, X = map(int, input().split())
lst = list(map(int, input().split()))
res = []
for i in lst:
    if X > i:
        res.append(i)
for j in res:
    print(j, end=' ')