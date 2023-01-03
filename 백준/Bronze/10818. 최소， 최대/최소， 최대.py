N = int(input())
lst = list(map(int, input().split()))
min = lst[0]
max = lst[0]

for i in range(N):
    if max < lst[i]:
        max = lst[i]
for j in range(N):
    if min > lst[j]:
        min = lst[j]


print(min, max)        
        