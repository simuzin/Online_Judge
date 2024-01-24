def solution(keymap, targets):
    answer = [0] * len(targets)
    temp = {'A':float('inf'),'B':float('inf'),'C':float('inf'),'D':float('inf'),'E':float('inf'),'F':float('inf'),'G':float('inf'),'H':float('inf'),'I':float('inf'),'J':float('inf'),'K':float('inf'),'L':float('inf'),'M':float('inf'),'N':float('inf'),'O':float('inf'),'P':float('inf'),'Q':float('inf'),'R':float('inf'),'S':float('inf'),'T':float('inf'),'U':float('inf'),'V':float('inf'),'W':float('inf'),'X':float('inf'),'Y':float('inf'),'Z':float('inf')}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            temp[keymap[i][j]] = min(temp[keymap[i][j]], j+1)
    for i in range(len(targets)):
        for j in range(len(targets[i])):
            if temp[targets[i][j]] != float('inf'):
                answer[i] += temp[targets[i][j]]
            else:
                answer[i] = -1
                break
    return answer