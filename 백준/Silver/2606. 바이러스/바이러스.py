def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()        
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
stack = []
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
dfs(1)
print(visited.count(True)-1)