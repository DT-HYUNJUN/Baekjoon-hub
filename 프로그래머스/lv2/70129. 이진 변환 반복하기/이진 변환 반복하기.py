def solution(S):
    answer = []
    zero_count = 0
    count = 0
    while 1:
        if S == '1':
            break
        zero_count += S.count('0')
        S = S.replace('0', '')
        S = bin(len(S))[2:]
        count += 1
        
    answer = [count, zero_count]
    return answer