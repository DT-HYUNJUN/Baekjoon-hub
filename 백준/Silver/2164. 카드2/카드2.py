from collections import deque
deq = deque(range(1, int(input())+1))
while len(deq) != 1:
    deq.popleft()
    deq.rotate(-1)
print(deq[0])