str = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
for i in alp:
    if i in str:
        print(str.index(i), end=' ')
    else:
        print(-1, end=' ')