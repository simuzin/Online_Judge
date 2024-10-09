import sys

k = int(sys.stdin.readline().strip())
stack = []
for _ in range(k):
    money = int(sys.stdin.readline().strip())
    if money:
        stack.append(money)
    else:
        stack.pop()
print(sum(stack))