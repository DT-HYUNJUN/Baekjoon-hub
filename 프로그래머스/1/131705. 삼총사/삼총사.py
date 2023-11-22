from itertools import combinations

def solution(number):
    answer = 0
    perm = list(combinations(number, 3))
    for i in perm:
        if sum(list(i)) == 0:
            answer += 1
    return answer