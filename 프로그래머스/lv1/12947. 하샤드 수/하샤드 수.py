def solution(x):
    answer = False
    tmp = sum(map(int, list(str(x))))
    if x % tmp == 0:
        answer = True
    return answer