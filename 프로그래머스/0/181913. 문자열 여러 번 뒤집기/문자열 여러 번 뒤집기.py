def solution(my_string, queries):
    for a, b in queries:
        answer, temp ='', ''
        answer += my_string[:a]
        temp = my_string[a:b+1]
        answer += temp[::-1]
        answer += my_string[b+1:]
        my_string = answer
    return my_string