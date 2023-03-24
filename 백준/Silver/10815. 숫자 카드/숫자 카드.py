N = int(input())
N_lst = sorted([int(x) for x in input().split()])
M = int(input())
M_lst = [int(x) for x in input().split()]
res = [0] * M
index = 0

def binary_search(lst, value):
    start, end = 0, N-1
    while start <= end:
        mid = int((start + end) / 2)
        if lst[mid] == value:
            return True
        if lst[mid] > value:
            end = mid - 1
        if lst[mid] < value:
            start = mid + 1

for i in M_lst:
    if binary_search(N_lst, i) == True:
        res[index] = 1
    index += 1
print(*res)