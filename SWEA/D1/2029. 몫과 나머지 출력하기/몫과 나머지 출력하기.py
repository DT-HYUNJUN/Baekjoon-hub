T = int(input())
for case in range(1, T+1):
    a, b = map(int, input().split())
    print("#%d %d %d" % (case, *divmod(a, b)))