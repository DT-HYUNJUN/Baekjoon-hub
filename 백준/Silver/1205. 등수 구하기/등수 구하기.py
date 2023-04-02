N, score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    lst = [int(x) for x in input().split()]
    rank = 0
    if lst[-1] >= score and N == P:
        print(-1)
    else:
        for i in lst:
            rank += 1
            if score >= i:
                print(rank)
                break
        else:
            print(rank+1)