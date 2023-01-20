T = int(input())
for _ in range(T):     
    PS = input()
    while '()' in PS:
        PS = PS.replace('()', '')
    if len(PS):
        print('NO')
    else:
        print('YES')
