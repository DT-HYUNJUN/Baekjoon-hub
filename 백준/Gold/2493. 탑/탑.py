N = int(input())
tower = [int(x) for x in input().split()]
stack = []
for i in range(N):
    while stack:
        if stack[-1][1] >= tower[i]:
            print(stack[-1][0] + 1, end=' ')
            break
        else:
            stack.pop()
    if not stack:
        print(0, end=' ')
    stack.append([i, tower[i]])