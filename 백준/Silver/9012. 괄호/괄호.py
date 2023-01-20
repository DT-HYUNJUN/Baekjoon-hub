T = int(input())
for _ in range(T):     
    PS = input()
    while '()' in PS:
        PS = PS.replace('()', '')
    print('NO' if len(PS) else 'YES')