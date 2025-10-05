import sys
input = sys.stdin.readline

N, M =map(int, input().split())

result = []

def recur(depth):
    if depth == M:
        print(*result)
        return

    for i in range(1, N+1):
        result.append(i)
        recur(depth+1)
        result.pop()

recur(0)