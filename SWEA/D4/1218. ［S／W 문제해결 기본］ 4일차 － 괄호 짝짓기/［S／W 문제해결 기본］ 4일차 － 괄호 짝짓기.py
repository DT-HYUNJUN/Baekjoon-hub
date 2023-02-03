T = 10
for test_case in range(1, T+1):
    N = int(input())
    PS = input()
    stack = []
    for i in PS:
        if i == '(' or i == '[' or i == '{' or i == '<':
            stack.append(i)
        elif i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                print(f'#{test_case} 0')
                break
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                print(f'#{test_case} 0')
                break
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                print(f'#{test_case} 0')
                break
        elif i == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                print(f'#{test_case} 0')
                break
    else:
        if stack:
            print(f'#{test_case} 0')
        else:
            print(f'#{test_case} 1')