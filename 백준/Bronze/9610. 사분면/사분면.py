N = int(input())
dic = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0, 'AXIS': 0}
for i in range(N):
    A, B = map(int, input().split())
    if A*B == 0:
        dic['AXIS'] += 1
    elif A>0 and B>0:
        dic['Q1'] += 1
    elif A<0 and B>0:
        dic['Q2'] += 1
    elif A<0 and B<0:
        dic['Q3'] += 1
    else:
        dic['Q4'] += 1
for key in dic:
    print(f'{key}: {dic[key]}')