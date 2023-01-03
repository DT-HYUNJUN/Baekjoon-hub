C = int(input())
for _ in range(C):
    cnt = 0
    lst = list(map(int, input().split()))
    avg = sum(lst[1:])/lst[0]    
    for i in lst[1:]:
        if i > avg:
            cnt += 1
    pct = (cnt/lst[0])*100
    print(f'{pct:.3f}%')
        