def solution(myString):
    answer = []
    temp = myString.split('x')
    for string in temp:
        if string == '':
            continue
        answer.append(string)          
    answer.sort()
    return answer