N = int(input())
rect = [[0]*101 for _ in range(101)]
cnt = 0
for _ in range(N):
    A, B = map(int, input().split())
    for i in range(A, A+10):
        for j in range(B, B+10):
            if rect[i][j] >= 1:
                pass
            else:
                rect[i][j] += 1             
                cnt += 1
print(cnt)