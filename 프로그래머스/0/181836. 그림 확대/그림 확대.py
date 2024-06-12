def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        temp = ''
        for j in range(len(picture[0])):  
            temp += picture[i][j] * k
        for l in range(k):
            answer.append(temp)
    return answer