import sys
input = sys.stdin.readline

N,M = map(int, input().split())

result = []
visited = [False] * (N+1)

def recur(start, depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(start, N+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            recur(i+1 ,depth+1)
            visited[i] = False
            result.pop()

recur(1, 0)