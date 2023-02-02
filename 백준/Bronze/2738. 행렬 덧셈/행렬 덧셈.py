import sys
N, M = map(int, sys.stdin.readline().split())
A = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
B = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]
for i in range(N):
    print(*[A[i][j] + B[i][j] for j in range(M)])