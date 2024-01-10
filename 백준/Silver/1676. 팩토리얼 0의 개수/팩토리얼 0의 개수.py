n = int(input())
temp = 1
if n == 0:
    print("0")
else:
    for i in range(1, n+1):
        temp *= i
    key = list(str(temp))[::-1]
    for i in range(len(key)):
        if key[i] != '0':
            print(i)
            break