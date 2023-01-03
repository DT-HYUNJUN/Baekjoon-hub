import sys

T = int(input())

for test_case in range(1, T+1):
    cnt, sum = 0, 0
    str = sys.stdin.readline()
    for i in str:
        if i == 'O':
            cnt += 1
            sum += cnt
        elif i == 'X':            
            cnt = 0
    print(sum)            