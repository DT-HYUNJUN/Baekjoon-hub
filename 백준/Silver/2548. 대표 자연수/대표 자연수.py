N = int(input())
lst = sorted([int(x) for x in input().split()])

if N & 1:
    print(lst[int(N/2)])
else:
    print(lst[int(N/2)-1])