A, B = map(int, input().split())
A_lst = [int(x) for x in input().split()]
B_lst = [int(x) for x in input().split()]
print(len(set(A_lst) ^ set(B_lst)))