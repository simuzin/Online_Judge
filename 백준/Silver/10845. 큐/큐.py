import sys
n = int(sys.stdin.readline().strip())
queue = []
for _ in range(n):
    s = sys.stdin.readline().strip()
    if s == 'pop':
        if len(queue):
            print(queue[0])
            del queue[0]
        else:
            print("-1")
    elif s == 'size':
        print(len(queue))
    elif s == 'empty':
        if len(queue):
            print("0")
        else:
            print("1")
    elif s == 'front':
        if len(queue):
            print(queue[0])
        else:
            print("-1")
    elif s == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print("-1")
    else:
        _,i = s.split()
        queue.append(int(i))