N, M = map(int, input().split())
lst = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for i in range(i-1, j):
        lst[i] = k
print(*lst)