N = int(input())
lst = [int(x) for x in input().split()]
res = []
cnt = 0
for i in lst:
    if i not in res:
        res.append(i)
    else:
        cnt += 1
print(cnt)