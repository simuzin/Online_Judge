n = input()
res = []
for num in n:
    res.append(int(num))
res.sort(reverse = True)
print(''.join(str(i) for i in res))
