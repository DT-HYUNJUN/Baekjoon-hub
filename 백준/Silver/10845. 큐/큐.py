import sys
N = int(sys.stdin.readline())
queue = []
for _ in range(N):
    string = sys.stdin.readline().split()
    command = string[0]

    if command == 'push':
        num = string[1]
        queue.append(num)
    
    elif command == 'pop':
        print(queue.pop(0) if len(queue) else -1)        
    
    elif command == 'size':
        print(len(queue))
    
    elif command == 'empty':
        print(0 if len(queue) else 1)
    
    elif command == 'front':
        print(queue[0] if len(queue) else -1)

    elif command == 'back':
        print(queue[-1] if len(queue) else -1)