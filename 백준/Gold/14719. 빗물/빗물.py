H, W = map(int, input().split())
lst = [int(x) for x in input().split()]

res = 0

for i in range(1, W-1):
    left = max(lst[:i])
    right = max(lst[i+1:])
    
    tmp = min(left, right)
    
    if lst[i] < tmp:
        res += tmp - lst[i]
print(res)