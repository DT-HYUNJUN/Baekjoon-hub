import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])