def solution(s):
    answer, key = [], {}
    temp = list(set(s))
    for c in temp:
        key[c] = float('inf')
        
    for i, c in enumerate(s):
        if key[c] == float('inf'):
            answer.append(-1)
            key[c] = i
        else:
            answer.append(i - key[c])
            key[c] = i
    return answer