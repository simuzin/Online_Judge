def solution(n):
    answer = [i for i in range(1,n+1)]
    answer = answer[::2]
    return answer