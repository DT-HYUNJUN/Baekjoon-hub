import sys
from collections import deque
N = int(sys.stdin.readline())
lst = deque()
while 1:
    num = int(sys.stdin.readline())
    if num == -1:
        break
    elif num != 0:
        if len(lst) == N:
            lst.popleft()
            lst.append(num)
        else:
            lst.append(num)
    elif num == 0:
        if lst:
            lst.popleft()    
if lst:
    print(*lst)
else:
    print('empty')