N, M = map(int, input().split())
lst = [[x for x in input()] for _ in range(N)]
cnt = []
for i in range(N-7):
    for j in range(M-7):
        cnt_W = 0
        cnt_B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) & 1:
                    if lst[k][l] != 'B':
                        cnt_W += 1
                    if lst[k][l] != 'W':
                        cnt_B += 1
                else:
                    if lst[k][l] != 'W':
                        cnt_W += 1
                    if lst[k][l] != 'B':
                        cnt_B += 1
        cnt.append(min(cnt_W, cnt_B))
print(min(cnt))