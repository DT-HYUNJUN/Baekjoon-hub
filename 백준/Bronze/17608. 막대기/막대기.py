import sys
N = int(input())
lst = [int(sys.stdin.readline()) for _ in range(N)]
standard = lst[-1]
cnt = 1
for i in reversed(lst):
    if  i > standard:
        cnt += 1
        standard = i
print(cnt)