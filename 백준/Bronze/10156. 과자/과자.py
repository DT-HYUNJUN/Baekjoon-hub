K, N, M = map(int, input().split())
sum = K*N-M
if sum < 0:
    print(0)
else:
    print(sum)