X = int(input())
N = int(input())
res = 0
for _ in range(N):
    a, b = map(int, input().split())
    res += a*b
if res == X:
    print('Yes')
else:
    print('No')    