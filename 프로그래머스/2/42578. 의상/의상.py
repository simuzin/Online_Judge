from itertools import combinations
def solution(clothes):
    answer = 1
    coni = {}
    for c_name, c_type in clothes:
        if c_type not in coni:
            coni[c_type] = 1
        coni[c_type] += 1
        
    for c in coni:
        answer *= coni[c]  
        
    return answer-1