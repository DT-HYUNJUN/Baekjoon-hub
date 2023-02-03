T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    puzzle_r = [[int(x) for x in input().split()] for _ in range(N)]
    puzzle_c = list(map(list, zip(*puzzle_r)))
    cnt = 0
    temp = ''
    for i in puzzle_r:
        temp = ''.join(map(str, i))
        lst = temp.split('0')
        cnt += lst.count('1'*K)
    for i in puzzle_c:
        temp = ''.join(map(str, i))
        lst = temp.split('0')
        cnt += lst.count('1'*K)            
    print(f'#{test_case} {cnt}')