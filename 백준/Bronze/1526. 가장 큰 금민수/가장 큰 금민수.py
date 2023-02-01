N = int(input())
gold = set('47')
for i in range(N,1,-1):
    num_set = set(str(i))
    if num_set & gold == num_set:
        print(i)
        break