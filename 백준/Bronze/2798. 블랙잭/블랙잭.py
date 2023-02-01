N, M = map(int, input().split())
lst = sorted([int(x) for x in input().split()], reverse=True)

maximum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            num = lst[i]+lst[j]+lst[k]
            if num <= M:
                if maximum < num:
                    maximum = num
                    break
print(maximum)