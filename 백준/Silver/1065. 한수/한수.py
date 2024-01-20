n = int(input())
if n//100 == 0:
    print(n)
else:
    res = 99
    for i in range(100, n+1):
        temp = str(i)
        if len(temp) == 3:
            if (int(temp[1]) - int(temp[0])) == (int(temp[2]) - int(temp[1])):
                res += 1
    print(res)