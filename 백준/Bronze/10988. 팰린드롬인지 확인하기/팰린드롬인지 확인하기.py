string = input()
for i in range(len(string)):
    if string[i] != string[-i-1]:
        print(0)
        break
else:
    print(1)