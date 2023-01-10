T = int(input())
for _ in range(T):
    Y = K = 0
    for i in range(9):
        A, B = map(int, input().split())
        Y += A
        K += B
    if Y > K:
        print('Yonsei')
    elif Y < K:
        print('Korea')
    else:
        print('Draw')