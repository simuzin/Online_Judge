key = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}
temp, answer = [], ''
for _ in range(3):
    temp.append(input())
answer += str(key[temp[0]])
answer += str(key[temp[1]])
print(int(answer) * (10**key[temp[2]]))