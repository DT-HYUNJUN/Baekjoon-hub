N = int(input())
lst = sorted([int(x) for x in input().split()])
res = 0
for i in range(N):
    res += sum(lst[0:i+1])
print(res)