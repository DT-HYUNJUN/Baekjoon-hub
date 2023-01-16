N = int(input())
lst = list(map(int, input().split()))
res, cnt = 0, 1
for i in lst:
    if i == 1:
        res += cnt
    else:
        cnt = 0
    cnt += 1
print(res)