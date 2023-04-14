T = int(input())
for _ in range(T):
    N = int(input())
    cant = []
    for i in range(2, 65):
        lst = []
        tmp = N
        while tmp != 0:
            lst.append(tmp % i)
            tmp  //= i
        
        for j in range(len(lst) // 2):
            if lst[j] != lst[-1-j]:
                cant.append(1)
                break
    if len(cant) == 63:
        print(0)
    else:
        print(1)