lst = [['*'] * 15 for _ in range(5)]
for i in range(5):
    temp = list(input().strip())
    for j in range(len(temp)):
        lst[i][j] = temp[j]

for i in range(15):
    for j in range(5):
        if lst[j][i] != '*':
            print(lst[j][i], end='')
        else:
            continue