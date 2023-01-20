T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [int(x) for x in input().split()]
    avg = sum(lst) // len(lst)
    cnt = 0
    for i in lst:
        if i <= avg:
            cnt += 1
    print(f'#{test_case} {cnt}')