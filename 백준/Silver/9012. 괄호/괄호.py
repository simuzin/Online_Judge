import sys
n = int(sys.stdin.readline())
for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    stack = []
    for i in temp:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')

    print("NO" if stack else "YES")