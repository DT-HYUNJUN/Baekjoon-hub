S = input()
N = int(input())
cnt = 0
for _ in range(N):
    ring = input()
    ring += ring
    if S in ring:
        cnt += 1
print(cnt)