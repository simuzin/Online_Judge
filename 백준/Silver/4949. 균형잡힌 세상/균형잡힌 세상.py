import sys
while True:
    temp = sys.stdin.readline().rstrip()
    if temp == '.':
        break
    stack = []
    for i in temp:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
        elif i == '[':
            stack.append('[')
        elif i == ']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(']')

    print("no" if stack else "yes")