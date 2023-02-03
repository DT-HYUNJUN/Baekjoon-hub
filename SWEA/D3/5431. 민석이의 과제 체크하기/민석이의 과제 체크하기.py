T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    reported = [int(x) for x in input().split()]
    res = []
    for i in range(1, N+1):
        if i not in reported:
            res.append(i)
    print(f'#{test_case}', *res)