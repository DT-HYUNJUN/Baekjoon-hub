rect = [[0]*101 for _ in range(101)]
cnt = 0
for _ in range(4):
    A, B, C, D = map(int, input().split())
    for i in range(A, C):
        for j in range(B, D):
            if rect[i][j] >= 1:
                pass
            else:
                rect[i][j] += 1             
                cnt += 1
print(cnt)