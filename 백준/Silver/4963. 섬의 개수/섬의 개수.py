import sys
sys.setrecursionlimit(10000)
def dfs(y, x):
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    if field[y][x] == 1:
        field[y][x] = 0
        dfs(y,   x-1)
        dfs(y,   x+1)
        dfs(y-1, x)
        dfs(y+1, x)
        dfs(y+1, x-1)
        dfs(y+1, x+1)
        dfs(y-1, x-1)
        dfs(y-1, x+1)
        return True
    return False    

while 1:
    w, h = map(int, input().split())    
    if w == 0 and h == 0:
        break
    field = [[int(x) for x in input().split()] for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                cnt += 1
    print(cnt)