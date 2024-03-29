N = int(input())
N_lst = sorted([int(x) for x in input().split()])
M = int(input())
M_lst = [int(x) for x in input().split()]

def binary_search_first(lst, value):
    start, end = 0, N-1
    while start <= end:
        mid = int((start + end) / 2)
        if lst[mid] == value:
            end = mid - 1
        if lst[mid] > value:
            end = mid - 1
        if lst[mid] < value:
            start = mid + 1
    return end
def binary_search_last(lst, value):
    start, end = 0, N-1
    while start <= end:
        mid = int((start + end) / 2)
        if lst[mid] == value:
            start = mid + 1
        if lst[mid] > value:
            end = mid - 1
        if lst[mid] < value:
            start = mid + 1
    return end


for i in M_lst:
    first = binary_search_first(N_lst, i)
    last = binary_search_last(N_lst, i)
    print(last - first, end=' ')