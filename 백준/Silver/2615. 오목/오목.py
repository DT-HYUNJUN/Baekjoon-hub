dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
graph = [[int(x) for x in input().split()] for _ in range(19)]

def check(x, y, num):

    for d in range(4):
        cnt = 1
        nx = x + dx[d]
        ny = y + dy[d]
        while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == num:
            cnt += 1
            if cnt == 5:
                if 0 <= x - dx[d] < 19 and 0 <= y - dy[d] < 19 and graph[x - dx[d]][y - dy[d]] == num:
                    break
                if 0 <= (nx + dx[d]) < 19 and 0 <= (ny + dy[d]) < 19 and graph[nx + dx[d]][ny + dy[d]] == num:
                    break

                print(num)
                print(x+1, y+1)
                return True
            nx += dx[d]
            ny += dy[d]


IS_BREAK = False

for i in range(19):
    for j in range(19):
        if graph[i][j] == 1:
            if check(i, j, 1):
                IS_BREAK = True
                break
        if graph[i][j] == 2:
            if check(i, j, 2):
                IS_BREAK = True
                break
    if IS_BREAK:
        break
else:
    print(0)