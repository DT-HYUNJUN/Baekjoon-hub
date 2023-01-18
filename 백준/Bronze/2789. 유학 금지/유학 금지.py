string = input()
censored = 'CAMBRIDGE'
for i in string:
    if i not in censored:
        print(i, end='')