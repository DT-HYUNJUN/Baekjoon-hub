import sys
import heapq
N = int(input())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        print(heapq.heappop(heap) if heap else 0)