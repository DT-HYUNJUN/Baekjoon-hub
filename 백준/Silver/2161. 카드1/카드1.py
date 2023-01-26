from collections import deque
N = int(input())
q = deque(range(1, N+1))
res = []
while len(q) != 1:
    res.append(q.popleft())
    q.append(q.popleft())
print(*res, *q)