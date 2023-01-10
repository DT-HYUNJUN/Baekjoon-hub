T = int(input())
for test_case in range(1, T+1):
    ls = list(map(int, input().split()))
    max = ls[0]
    for i in ls:
        if max < i:
            max = i
    print(f'#{test_case} {max}')