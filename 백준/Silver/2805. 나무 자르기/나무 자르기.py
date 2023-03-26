N, M = map(int, input().split())
tree = sorted([int(x) for x in input().split()])

def binary_search():
    start = 0
    end = tree[-1]
    while start <= end:
        mid = int((start + end) / 2)
        tmp = 0
        for i in tree:
            if i >= mid:
                tmp += i - mid
        if tmp >= M:
            start = mid + 1
        else:
            end = mid - 1
    print(end)
binary_search()