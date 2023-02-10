T = int(input())
for test_case in range(1, T+1):
    string = input().strip()
    dic = {}
    res = 'No'
    
    for char in string:
        dic[char] = dic.get(char, 0) + 1
    
    if len(dic) == 2:
        for k in dic:
            if dic[k] == 2:
                res = 'Yes'
                
    print(f'#{test_case} {res}')