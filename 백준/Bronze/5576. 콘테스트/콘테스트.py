lst = [int(input()) for _ in range(20)]
print(sum(sorted(lst[:10])[-3:]), sum(sorted(lst[10:])[-3:]))