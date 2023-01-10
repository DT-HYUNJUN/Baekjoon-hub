while True:
    factor = []
    n = int(input())
    if n == -1:
        break
    else:
        for i in range(1, n):
            if n%i == 0:
                factor.append(i)
        if sum(factor) == n:
            print(n, '=', 1, end=' ')
            for j in factor[1:]:
                print('+', j, end =' ')
            print()
        else:
            print(n, 'is NOT perfect.')