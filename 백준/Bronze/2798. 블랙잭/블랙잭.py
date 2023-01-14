N, M = map(int, input().split())
lst = list(map(int, input().split()))
Sum = []
for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            num = lst[i]+lst[j]+lst[k]
            if num <= M:
                Sum.append(num)                
print(sorted(Sum)[-1])