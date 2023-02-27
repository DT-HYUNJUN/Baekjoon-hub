def sqr(side):
    for i in range(N-side+1):
        for j in range(M-side+1):
            if matrix[i][j] == matrix[i+side-1][j] == matrix[i+side-1][j+side-1] == matrix[i][j+side-1]:
                return True
    return False

N, M = map(int, input().split())
matrix = [[int(x) for x in input()] for _ in range(N)]

side = min(N, M)

for i in range(side, 0, -1):
    if sqr(i) == True:
        print(i**2)
        break