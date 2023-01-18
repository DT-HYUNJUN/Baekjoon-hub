lst = [int(x) for x in input().split()]
compare = [1, 2, 3, 4, 5]
i = 0
while lst != compare:
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            print(*lst)