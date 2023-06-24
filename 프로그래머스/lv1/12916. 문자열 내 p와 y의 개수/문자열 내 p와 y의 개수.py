def solution(S):
    answer = True
    S = S.lower()
    if S.count('p') + S.count('y') == 0:
        answer = True
    elif S.count('p') != S.count('y'):
        answer = False
    return answer