def solution(my_string):
    answer = []
    for i in reversed(range(len(my_string))):
        answer.append(my_string[i:])
    answer.sort()
    return answer