T = int(input())
for test_case in range(1, T+1):
    string = input()
    reverse = string[::-1]
    res = ''
    for char in reverse:
        if char == 'b':
            res += 'd'
        if char == 'd':
            res += 'b'
        if char == 'p':
            res += 'q'
        if char == 'q':
            res += 'p'
    print(f'#{test_case} {res}')