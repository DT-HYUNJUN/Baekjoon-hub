from collections import deque
T = 10
for t in range(1, T+1):
    case = int(input())
    queue = deque([int(x) for x in input().split()])
    subtract = 1
    while 1:
        if subtract > 5:
            subtract = 1
        num = queue.popleft() - subtract
        if num <= 0:
            queue.append(0)
            break
        queue.append(num)
        subtract += 1  
    print(f'#{case}', *queue)