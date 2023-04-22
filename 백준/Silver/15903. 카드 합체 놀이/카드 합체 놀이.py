N, M = map(int, input().split())
lst = [int(x) for x in input().split()]

for i in range(M):
    lst = sorted(lst)
    tmp = lst[0] + lst[1]
    lst[0] = tmp
    lst[1] = tmp
print(sum(lst))