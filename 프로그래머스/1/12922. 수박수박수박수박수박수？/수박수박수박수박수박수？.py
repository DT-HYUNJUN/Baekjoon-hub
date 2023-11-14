def solution(n):
    h, t = divmod(n, 2)
    if t:
        return '수박' * h + '수'
    else:
        return '수박' * h
        