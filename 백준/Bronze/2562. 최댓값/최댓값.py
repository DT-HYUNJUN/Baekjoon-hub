lst = []
max = 0
for _ in range(9):
    num = int(input())
    lst.append(num)
    if max < num:
        max = num
        
print(max)
print(lst.index(max)+1)