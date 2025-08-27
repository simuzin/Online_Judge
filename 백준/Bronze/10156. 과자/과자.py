import sys

K, N, M = map(int, sys.stdin.readline().split())
answer = M - (K * N)
print(0 if answer > 0 else abs(answer))