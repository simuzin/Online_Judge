import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

result = []

def recur(depth, current, plus, minus, multi, div):
    if depth == N:
        result.append(current)
        return

    if plus > 0:
        recur(depth+1, current + A[depth], plus-1, minus, multi, div)
    if minus > 0:
        recur(depth+1, current - A[depth], plus, minus-1, multi, div)
    if multi > 0:
        recur(depth+1, current * A[depth], plus, minus, multi-1, div)
    if div > 0:
        if current > 0:
            recur(depth+1, current // A[depth], plus, minus, multi, div-1)
        else:
            recur(depth + 1, - (-current // A[depth]), plus, minus, multi, div-1)

recur(1, A[0], plus, minus, multi, div)
print(max(result))
print(min(result))