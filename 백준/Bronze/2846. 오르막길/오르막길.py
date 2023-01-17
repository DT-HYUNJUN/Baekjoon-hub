N = int(input())
lst = [int(x) for x in input().split()]
res = []
total = 0
for i in range(1, N):
    if lst[i-1] < lst[i]:
        total += lst[i] - lst[i-1]
    else:
        total = 0    
    res.append(total)
print(max(res))