N, M = map(int, input().split())
lst = [0] + [int(x+1) for x in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    lst[j], lst[i] = lst[i], lst[j]
print(*lst[1:])