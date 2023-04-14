T = int(input())
for _ in range(T):
    IS_PALL = False
    IS_BREAK = False
    k = int(input())
    lst = [input() for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            S = lst[i] + lst[j]
            for c in range(len(S)//2):
                if S[c] != S[-1-c]:
                    break
            else:
                print(S)
                IS_PALL = True
                IS_BREAK = True
                break
        if IS_BREAK:
            break
    if not IS_PALL:
        print(0)