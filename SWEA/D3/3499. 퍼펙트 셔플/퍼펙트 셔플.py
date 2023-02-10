T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = [x for x in input().split()]
    res = []
    
    if N & 1 == 1:
        half = int(N/2)+1
    else:
        half = int(N/2)
        
    for i in range(half):
        res.append(lst[i])
        if i+half == N:
            break
        res.append(lst[i+half])
    print(f'#{test_case}', *res)