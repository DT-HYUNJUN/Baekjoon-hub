import sys
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
print(*lst, sep='\n')