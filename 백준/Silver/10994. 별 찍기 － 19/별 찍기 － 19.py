def rec(N, x, y):
    row = N * 4 - 3
    if N == 1:
        lst[x][y] = '*'
        return
    for i in range(row):
        lst[x][y + i] = '*'
        lst[x+i][y] = '*'
        lst[x+row-1][y+i] = '*'
        lst[x+i][y+row-1] = '*'        
    rec(N-1, x+2, y+2)

N = int(input())
row = N * 4 - 3
lst = [[' ' for _ in range(row)] for _ in range(row)]
rec(N, 0, 0)
for i in lst:
    print(''.join(i))