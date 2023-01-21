import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    string = sys.stdin.readline().split()
    command = string[0]

    if command == 'push':
        num = string[1]
        stack.append(num)
    
    elif command == 'pop':
        print(stack.pop() if len(stack) else -1)        
    
    elif command == 'size':
        print(len(stack))
    
    elif command == 'empty':
        print(0 if len(stack) else 1)
    
    elif command == 'top':
        print(stack[-1] if len(stack) else -1)