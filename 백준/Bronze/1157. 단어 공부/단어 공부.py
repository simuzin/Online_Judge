a = input().upper()
temp = list(set(a))
key = []
for i in temp:
    key.append(a.count(i))

flag = key.count(max(key))

if flag == 1:
    print(temp[key.index(max(key))])
else:
    print("?")