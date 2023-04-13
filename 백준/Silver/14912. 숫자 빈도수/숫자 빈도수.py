n, d = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if str(i).count(str(d)) > 0:
        cnt += str(i).count(str(d))
print(cnt)