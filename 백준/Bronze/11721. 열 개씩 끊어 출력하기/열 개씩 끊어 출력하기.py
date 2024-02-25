s = input()
x = len(s) // 10
for i in range(x+1):
    print(s[i*10:(i*10)+10])