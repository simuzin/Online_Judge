import sys

n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []
answer = []
current_cum = 1

for num in nums:
    while current_cum <= num:
        stack.append(current_cum)
        answer.append('+')
        current_cum += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        sys.exit()

print("\n".join(answer))