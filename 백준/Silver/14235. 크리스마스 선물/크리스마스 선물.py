import heapq
N = int(input())
heap = []
for _ in range(N):
    lst = [int(x) for x in input().split()]
    if lst[0] != 0:
        for i in range(lst[0]):            
            heapq.heappush(heap, -lst[i+1])
    else:
        if heap:
            print(-(heapq.heappop(heap)))
        else:
            print(-1)