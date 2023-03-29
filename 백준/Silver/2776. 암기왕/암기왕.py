def binary_search(value):
    start = 0
    end = N-1
    while start <= end:
        mid = int((start + end) / 2)
        if N_lst[mid] == value:
            return True
        if N_lst[mid] > value:
            end = mid - 1
        if N_lst[mid] < value:
            start = mid + 1
        

T = int(input())

for _ in range(T):
    N = int(input())
    N_lst = sorted([int(x) for x in input().split()])
    M = int(input())
    M_lst = [int(x) for x in input().split()]

    for i in M_lst:
        if binary_search(i) == True:
            print(1)
        else:
            print(0)