V = int(input())
lst = list(input())
A = lst.count('A')
B = lst.count('B')
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')