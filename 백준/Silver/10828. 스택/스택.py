import sys

n = int(sys.stdin.readline().strip())
stack = []
for _ in range(n):
    command = list(sys.stdin.readline().strip().split())
    if len(command) == 2:
        if command[0] == 'push':
            stack.append(int(command[1]))
    else:
        if command[0] == 'pop':
            if not stack:
                print("-1")
            else:
                print(stack.pop())
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'empty':
            if stack:
                print("0")
            else:
                print("1")
        elif command[0] == 'top':
            if not stack:
                print("-1")
            else:
                print(stack[-1])