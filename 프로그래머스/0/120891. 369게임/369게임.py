from collections import Counter
def solution(order):
    answer = 0
    temp = Counter(str(order))
    for cnt in temp:
        if cnt in ['3','6','9']:
            answer += temp[cnt]
    return answer