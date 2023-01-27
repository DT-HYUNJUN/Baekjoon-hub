status =''
stack = []
while 1:
    string = input()
    if string == '문제':
        stack.append(string)
    elif string == '고무오리':
        if stack:            
            stack.pop()
        else:
            stack.append('문제')
            stack.append('문제')
    elif string == '고무오리 디버깅 끝':
        print('힝구' if stack else '고무오리야 사랑해')
        break