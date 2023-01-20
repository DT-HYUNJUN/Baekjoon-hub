T = int(input())
for test_case in range(1, T+1):
    lst = [int(x) for x in input().split()]
    res = 0
    for i in lst:
        if lst.count(i) == 1 or lst.count(i) == 3:
            res = i
    print(f'#{test_case} {res}')