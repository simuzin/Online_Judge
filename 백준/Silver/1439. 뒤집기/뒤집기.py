import sys
s = sys.stdin.readline().strip()
stack = []
for num in s:
    stack.append(int(num))
    if stack[-2:] == [1,1] or stack[-2:] == [0,0]:
        stack.pop()
print(min(len(stack)-sum(stack), sum(stack)))