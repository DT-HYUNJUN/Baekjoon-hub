import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(N)]
B = [[int(x) for x in input().split()] for _ in range(N)]
for i in range(N):
    print(*[A[i][j] + B[i][j] for j in range(M)])