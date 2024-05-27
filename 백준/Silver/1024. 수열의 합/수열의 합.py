import sys

n,l = map(int, sys.stdin.readline().strip().split())
answer = []
for length in range(l, 101):
        # sum - (length * (length - 1) // 2) must be non-negative
        temp = n - (length * (length - 1) // 2)
        if temp < 0:
            continue
        # First element of the sequence
        if temp % length == 0:
            first = temp // length
            if first >= 0:
                answer.append([first + i for i in range(length)])
                break

if answer:
     print(*answer[0])
else:
     print("-1")