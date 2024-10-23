def solution(n, left, right):
    answer = []
    
    # 2차원 배열 구축
    for i in range(left, right+1):
        row = i // n + 1
        column = i % n + 1
        answer.append(max(row,column))
    
    return answer