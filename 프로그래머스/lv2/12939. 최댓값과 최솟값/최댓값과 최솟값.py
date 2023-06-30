def solution(S):
    answer = ''
    lst = [int(x) for x in S.split(' ')]
    answer = f'{min(lst)} {max(lst)}'
    return answer