T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    res = []
    cnt = 1
    while len(res) != 10:
        loop_N = cnt * N
        string_N = str(loop_N)
        for i in string_N:
            if i not in res:
                res.append(i)
        cnt += 1        
    print(f'#{test_case} {loop_N}')