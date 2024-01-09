temp = 1
answer = [0,0,0,0,0,0,0,0,0,0]
for i in range(3):
    temp *= (int(input()))
for i in range(len(str(temp))):
    answer[int(str(temp)[i])] += 1
for i in answer:
    print(i)