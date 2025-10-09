import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = []

def recur(start, depth, sum):
    if depth == 3:
        if sum <= M:
            result.append(sum)
        return
    for i in range(start, N):
        recur(i+1, depth+1, sum + cards[i])

recur(0,0,0)
print(max(result))