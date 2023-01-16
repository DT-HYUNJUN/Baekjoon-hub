import sys
N = int(input())
xy = []
for _ in range(N):
    xy.append(list(map(int, sys.stdin.readline().split())))
xy.sort(key=lambda x:(x[0], x[1]))
for i in range(N):
    print(*xy[i])