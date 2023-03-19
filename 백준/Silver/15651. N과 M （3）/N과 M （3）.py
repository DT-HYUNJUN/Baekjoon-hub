def back():
    if len(lst) == M:
        print(*lst)
        return
    for i in range(1, N+1):
        # if i not in lst:
        lst.append(i)
        back()
        lst.pop()

N, M = map(int, input().split())
lst = []
back()