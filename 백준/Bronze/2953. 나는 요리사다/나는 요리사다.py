lst = [sum([int(x) for x in input().split()]) for _ in range(5)]
print(lst.index(max(lst))+1, max(lst))