N, M = map(int, input().split())
lst = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    lst[a][b] = 1
    lst[b][a] = 1
res = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        for k in range(j+1, N+1):
            if not lst[i][j] and not lst[j][k] and not lst[k][i]:
                res += 1
print(res)