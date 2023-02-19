def dfs_1(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == '-':
        graph[x][y] = 0
        dfs_1(x, y+1)
        dfs_1(x, y-1)
        return True
    return False

def dfs_2(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == '|':
        graph[x][y] = 0
        dfs_2(x+1, y)
        dfs_2(x-1, y)
        return True
    return False
    

N, M = map(int, input().split())
graph = [[x for x in input()] for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if dfs_1(i, j) == True:
            res += 1

for i in range(N):
    for j in range(M):
        if dfs_2(i, j) == True:
            res += 1
print(res)