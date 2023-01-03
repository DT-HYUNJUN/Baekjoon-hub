lst = []
for i in range(10):
    num = int(input())
    res = num % 42
    if res not in lst:
        lst.append(res)
print(len(lst))