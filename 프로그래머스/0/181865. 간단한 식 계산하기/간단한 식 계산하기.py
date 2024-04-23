def solution(binomial):
    answer = 0
    temp = binomial.split()
    if temp[1] == '+':
        answer = int(temp[0]) + int(temp[2])
    elif temp[1] == '-':
        answer = int(temp[0]) - int(temp[2])
    else:
        answer = int(temp[0]) * int(temp[2])
    return answer