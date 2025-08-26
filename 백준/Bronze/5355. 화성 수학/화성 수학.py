import sys

T = int(sys.stdin.readline())
for _ in range(T):
    temp = list(sys.stdin.readline().split())
    answer = float(temp[0])
    for i in range(1, len(temp)):
        if temp[i] =='@':
            answer *= 3
        elif temp[i] == '%':
            answer += 5
        elif temp[i] == '#':
            answer -= 7
    print("{:.2f}".format(answer))