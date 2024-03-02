def solution(my_string, s, e):
    answer = my_string[:s]
    temp = my_string[s:e+1]
    answer += temp[::-1]
    answer += my_string[e+1:]
    return answer