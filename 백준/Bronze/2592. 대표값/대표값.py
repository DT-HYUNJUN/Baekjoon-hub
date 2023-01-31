lst = [int(input()) for _ in range(10)]
print(sum(lst)//len(lst))
print(max(lst, key=lst.count))