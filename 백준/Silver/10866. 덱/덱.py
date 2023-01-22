import sys
N = int(sys.stdin.readline())
deque = []
for _ in range(N):
    string = sys.stdin.readline().split()
    command = string[0]

    if command == 'push_front':
        num = string[1]
        deque.insert(0, num)

    elif command == 'push_back':
        num = string[1]
        deque.append(num)
    
    elif command == 'pop_front':
        print(deque.pop(0) if len(deque) else -1)
    
    elif command == 'pop_back':
        print(deque.pop() if len(deque) else -1)
    
    elif command == 'size':
        print(len(deque))
    
    elif command == 'empty':
        print(0 if len(deque) else 1)
    
    elif command == 'front':
        print(deque[0] if len(deque) else -1)

    elif command == 'back':
        print(deque[-1] if len(deque) else -1)