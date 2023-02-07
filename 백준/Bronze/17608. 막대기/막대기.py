import sys
N = int(input())
lst = [int(sys.stdin.readline()) for _ in range(N)]
standard = lst[-1]
cnt = 1
for i in range(N-1, -1, -1):
    if  lst[i] > standard:
        cnt += 1
        standard = lst[i]
print(cnt)