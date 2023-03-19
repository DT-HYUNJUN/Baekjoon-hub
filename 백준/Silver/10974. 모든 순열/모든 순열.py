N = int(input())
lst = []
def back():
    if len(lst) == N:
        print(*lst)
        return
    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            back()
            lst.pop()
back()