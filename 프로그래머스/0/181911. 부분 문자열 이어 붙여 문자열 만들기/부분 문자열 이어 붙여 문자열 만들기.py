def solution(my_strings, parts):
    answer = ''
    for i,data in enumerate(parts):
        answer += my_strings[i][data[0]:data[1]+1]
    return answer