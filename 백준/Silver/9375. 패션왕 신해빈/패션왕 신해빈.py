import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    clothes = {}
    for _ in range(n):
        a,b = sys.stdin.readline().strip().split()
        if b in clothes:
            clothes[b] += 1
        else:
            clothes[b] = 2

    answer = 1
    for wearing in clothes:
        answer *= clothes[wearing]
    print(answer-1)