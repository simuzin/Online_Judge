import sys
input = sys.stdin.readline

def recur(depth, start, S):
    if depth == 6:
        print(*result)
        return

    for i in range(start, len(S)):
        result.append(S[i])
        recur(depth+1,i+1, S)
        result.pop()


flag = False
while True:
    S = list(map(int, input().split()))
    if S[0] == 0:
        break
    else:
        if flag == True:
            print()
        k = S[0]
        S = S[1:]
        result = []
        flag = True

        recur(0,0, S)