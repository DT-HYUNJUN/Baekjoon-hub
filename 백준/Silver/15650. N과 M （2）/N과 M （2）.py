def back(s):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(s, N+1):
        if i not in lst:
            lst.append(i)
            back(i+1)
            lst.pop()

N, M = map(int, input().split())
lst = []
back(1)