_, k = map(int, input().split())
lst = sorted([int(x) for x in input().split()])
print(lst[-k])