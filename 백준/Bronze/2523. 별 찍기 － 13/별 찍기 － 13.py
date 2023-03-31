N = int(input())
STAR = '*'
for i in range(1, N+1):
    print(STAR * i)
for i in range(N-1, 0, -1):
    print(STAR * i)