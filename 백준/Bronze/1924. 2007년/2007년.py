month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
x, y = map(int, input().split())

date = 0
res = ''
for i in range(x-1):
    date += month[i]
date = (date + y) % 7
print(day[date])