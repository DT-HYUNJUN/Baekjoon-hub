T = int(input())
A_life = B_life = 100

for i in range(T):
    A, B = map(int, input().split())
    if A > B:
        B_life -= A
    elif A < B:
        A_life -= B
print(A_life, B_life, sep='\n')