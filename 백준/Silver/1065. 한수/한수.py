def func(a):
    cnt = 0
    for i in range(1, a+1):
        if i < 100:
            cnt += 1
        elif 1000> i >= 100:           
            lst = list(map(int, str(i)))
            for j in range(0, len(lst)-2):                
                if lst[j]-(lst[j+1]) == (lst[j+1])-(lst[j+2]):
                    cnt += 1
    return cnt
N = int(input())
res = func(N)
print(res)