N, K = map(int, input().split())
lst = [int(x) for x in input().split()]
window = sum(lst[:K])
res = window

for i in range(K, N):
    window += lst[i] - lst[i-K]
    res = max(res, window)
print(res)