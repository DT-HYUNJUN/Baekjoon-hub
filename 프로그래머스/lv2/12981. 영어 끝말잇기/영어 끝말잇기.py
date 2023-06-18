def p_answer(i, n):
    return [(i % n) + 1, int((i + n) / n)]
    
def solution(n, words):
    used = [words[0]]
    for i in range(1, len(words)):
        if len(words[i]) == 1:
            return p_answer(i, n)
        if words[i-1][-1] != words[i][0]:
            return p_answer(i, n)
        if words[i] in used:
            return p_answer(i, n)
        used.append(words[i])
    return [0, 0]