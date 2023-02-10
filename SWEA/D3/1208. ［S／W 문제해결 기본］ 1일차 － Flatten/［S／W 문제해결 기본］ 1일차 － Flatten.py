T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = [int(x) for x in input().split()]    
    cnt = 0
    res = 0
    
    while cnt != N:
        m = lst.index(max(lst))
        n = lst.index(min(lst))
        lst[m] -= 1
        lst[n] += 1
        cnt += 1
    
    res = max(lst) - min(lst)
    print(f'#{test_case} {res}')