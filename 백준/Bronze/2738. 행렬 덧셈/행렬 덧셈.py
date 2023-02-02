N, M = map(int, input().split())
matrix_A = [[int(x) for x in input().split()] for _ in range(N)]
matrix_B = [[int(x) for x in input().split()] for _ in range(N)]
res = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        print(matrix_A[i][j] + matrix_B[i][j], end=' ')
    print()