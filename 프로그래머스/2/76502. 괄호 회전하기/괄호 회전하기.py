from collections import deque
def solution(s):
    answer = 0
    queue = deque(s)
    key = [["{","}"],["[","]"],["(",")"]]
    for _ in range(len(s)):
        queue.rotate(-1)
        stack = []
        for n in queue:
            stack.append(n)
            if stack[-2:] in key:
                stack.pop()
                stack.pop()
        if not stack:
            answer += 1
    return answer