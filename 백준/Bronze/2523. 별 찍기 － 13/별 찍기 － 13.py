N = int(input())
STAR = '*'
for i in range(1-N, N):
    print(STAR * (N-abs(i)))