def solution(my_string):
    answer = ''  
    aeiou = ['a','e','i','o','u']
    for s in my_string:
        answer += s
        if s in aeiou:
            answer = answer[:-1]
    return answer