happy = ':-)'
sad = ':-('
string = input()
if string.count(happy) + string.count(sad) == 0:
    print('none')
elif string.count(happy) - string.count(sad) > 0:
    print('happy')
elif string.count(happy) - string.count(sad) < 0:
    print('sad')
else:
    print('unsure')