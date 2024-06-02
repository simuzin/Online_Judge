def solution(my_string):
    temp = my_string.split()
    stack = []
    
    flag = 0
    for i in temp:
        if i.isdigit():
            stack.append(int(i))
        elif i == '+':
            flag = 1
        elif i == '-':
            flag = 2
        
        if len(stack) >= 2:
            if flag == 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif flag == 2:
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            flag = 0
    return stack[0]