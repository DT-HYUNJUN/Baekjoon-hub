string = input()
sum = 0
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in croatia:
    if i in string:
        sum += string.count(i)
        string = string.replace(i, '1')        
print(len(string) + sum - string.count('1'))