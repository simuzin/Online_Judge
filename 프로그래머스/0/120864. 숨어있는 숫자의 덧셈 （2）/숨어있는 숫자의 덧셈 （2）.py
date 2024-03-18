def solution(my_string):
    answer = 0
    stack = []
    for i in my_string:
        if i.isdigit():
            stack.append(i)
        else:
            if stack:
                temp = ''.join(str(i) for i in stack)
                answer += int(temp)
                stack = []
    if stack:
        temp = ''.join(str(i) for i in stack)
        answer += int(temp)
    return answer