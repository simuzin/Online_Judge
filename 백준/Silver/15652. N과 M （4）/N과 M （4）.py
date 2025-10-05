import sys
input = sys.stdin.readline

N, M =map(int, input().split())

result = []

def recur(start, depth):
    if depth == M:
        print(*result)
        return

    for i in range(start, N+1):
        result.append(i)
        recur(i, depth+1)
        result.pop()

recur(1,0)