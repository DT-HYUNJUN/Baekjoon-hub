from collections import deque
N, K = map(int, input().split())

lst = deque(range(1, N+1))
res = []

while lst:
    for _ in range(K):
        lst.append(lst.popleft())
    res.append(lst.pop())

print(str(res).replace('[', '<').replace(']', '>'))