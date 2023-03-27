def binary_search(lst):
    start = 0
    end = max(lst) * M
    while start <= end:
        total = 0
        mid = int((start + end) / 2)
        for i in A:
            total += int(mid / i)        
        if total < M:
            start = mid + 1
        else:
            end = mid - 1
            res = mid
    print(res)


N, M = map(int, input().split())
A = [int(x) for x in input().split()]

binary_search(A)