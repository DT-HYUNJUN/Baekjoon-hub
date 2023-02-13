def dfs(start, cnt):
    global res
    cnt += 1
    visited[start] = True
    if start == B:
        res = cnt
    for i in graph[start]:
        if not visited[i]:
            dfs(i, cnt)    

n = int(input())
A, B = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res = 0

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
dfs(A, 0)

if res:
    print(res-1)
else:
    print(-1)