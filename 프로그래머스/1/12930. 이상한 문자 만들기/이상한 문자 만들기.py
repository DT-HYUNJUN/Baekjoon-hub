def solution(s):
    answer = []
    for word in s.split(' '):
        temp = ''
        for i in range(len(word)):
            if i & 1:
                temp += word[i].lower()
            else:
                temp += word[i].upper()
        answer.append(temp)
    return ' '.join(answer)