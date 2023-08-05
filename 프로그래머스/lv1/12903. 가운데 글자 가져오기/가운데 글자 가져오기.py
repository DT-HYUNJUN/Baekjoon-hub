def solution(s):
    answer = ''
    s_len = int(len(s) / 2)
    if len(s) % 2 != 0:
        return s[s_len]
    else:
        return s[s_len-1:s_len+1]
    return answer