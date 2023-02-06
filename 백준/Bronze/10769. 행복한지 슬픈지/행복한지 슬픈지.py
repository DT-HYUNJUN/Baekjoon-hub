happy = ':-)'
sad = ':-('
string = input()
h, s = string.count(happy), string.count(sad)
if h == s == 0:
    print('none')
elif h == s:
    print('unsure')
elif h > s:
    print('happy')
else:
    print('sad')