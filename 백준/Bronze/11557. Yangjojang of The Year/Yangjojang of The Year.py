T = int(input())
for _ in range(T):
    univ = []
    drink = []
    N = int(input())
    for _ in range(N):
        A, B = map(str, input().split())
        univ.append(A)
        drink.append(int(B))
    Max = drink[0]
    for i in drink:
        if Max < i:
            Max = i
    print(univ[(drink.index(Max))])