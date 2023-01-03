N = int(input())
lst = list(map(int, input().split()))
sum = 0
Max = lst[0]

for i in lst:
    if Max < i:
        Max = i

for j in lst:
    j = j/Max*100
    sum += j
    
print(sum/N)