T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    lst = [[int(x) for x in input().split()] for _ in range(m)]
    lst_trans = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            lst_trans[i][j] = lst[j][i]
             
    total = 0
    for i in range(n):
        cnt = 0
        for j in range(-1, -(m+1), -1):
            if lst_trans[i][j]:
                total += cnt
            else:
                cnt += 1
    print(total)