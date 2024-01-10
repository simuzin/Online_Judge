n = int(input())
temp, length = [], {}
for i in range(n):
    temp.append(input())
temp.sort()

for s in temp:
    length[s] = len(s)   
answer = dict(sorted(length.items(), key=lambda x: x[1]))
for key in answer.keys():
    print(key)