N = int(input())
gold = ('4', '7')
for i in range(N,1,-1):
    num_set = set(str(i))
    if num_set.intersection(gold) == num_set:
        print(i)
        break