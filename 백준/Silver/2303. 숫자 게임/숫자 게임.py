N = int(input())
card = [[] for _ in range(N)]
for t in range(N):
    max_num = 0
    lst = [int(x) for x in input().split()]
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                tmp = (lst[i] + lst[j] + lst[k]) % 10
                if max_num <= tmp:
                    max_num = tmp
                    card[t] = [max_num, (t+1)]    
print((sorted(card))[-1][1])