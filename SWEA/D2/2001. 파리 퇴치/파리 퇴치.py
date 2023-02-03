T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [[int(x) for x in input().split()] for _ in range(N)]
    max_ = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for a in range(M):
                for b in range(M):
                    fly += matrix[i+a][j+b]
            if max_ < fly:
                max_ = fly
    print(f'#{test_case} {max_}')