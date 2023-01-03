N = int(input())
lst = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in range(N):
    if v == lst[i]:
        cnt += 1
        
print(cnt)        