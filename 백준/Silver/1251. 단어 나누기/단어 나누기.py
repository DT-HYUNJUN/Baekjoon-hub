string = input()
res = []
for i in range(1, len(string)):
    for j in range(i+1, len(string)):        
        a = string[0:i][::-1]
        b = string[i:j][::-1]
        c = string[j:][::-1]
        res.append(a+b+c)
print(sorted(res)[0])