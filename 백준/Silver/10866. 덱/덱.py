import sys
from collections import deque

n = int(sys.stdin.readline())
temp = deque()
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s == 'size':
        print(len(temp))
    elif s == 'empty':
        if temp:
            print("0")
        else:
            print("1")
    elif s == 'front':
        if temp:
            print(temp[0])
        else:
            print("-1")
    elif s == 'back':
        if temp:
            print(temp[-1])
        else:
            print("-1")
    elif s == 'pop_front':
        if temp:
            print(temp.popleft())
        else:
            print("-1")
    elif s == 'pop_back':
        if temp:
            print(temp.pop())
        else:
            print("-1")
    else:
        a,b = s.split()
        if a == 'push_front':
            temp.appendleft(int(b))
        elif a == 'push_back':
            temp.append(int(b))
