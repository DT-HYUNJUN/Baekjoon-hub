def dfs(start):
    stack = [start]
    visited[start] = True
    while stack:
        cur = stack.pop()        
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
                
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    stack = []
    cnt = 0
    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for i in range(1, N+1):
        if visited[i] == False:
            dfs(i)
            cnt += 1    
    print(f'#{test_case} {cnt}')