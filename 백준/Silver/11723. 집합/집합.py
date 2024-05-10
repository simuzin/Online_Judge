import sys
m = int(sys.stdin.readline().strip())
S = set()
for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 2:
        a, b = temp
        b = int(b)

        if a == 'add':
            S.add(b)
        elif a == 'remove':
            if b in S:
                S.remove(b)
        elif a == 'check':
            if b in S:
                print(1)
            else:
                print(0)
        elif a == 'toggle':
            if b in S:
                S.remove(b)
            else:
                S.add(b)
    else:
        if temp[0] == 'all':
            S = set(range(1,21))
        else:
            S.clear()