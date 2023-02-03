T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score = []
    for i in range(N):
        a, b, c = map(int, input().split())
        score.append((a*35 + b*45 + c*20)/100)
    K_score = score[K-1]
    score.sort(reverse=True)
    res = score.index(K_score) // int(N/10)
    print(f'#{test_case} {grade[res]}')