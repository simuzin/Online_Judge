def solution(food):
    answer = ''
    temp = []
    for i in range(1,len(food)):
        for j in range(food[i] // 2):
            temp.append(i)
    temp.append(0)
    answer = temp + temp[-2::-1]
    return ''.join(map(str,answer))