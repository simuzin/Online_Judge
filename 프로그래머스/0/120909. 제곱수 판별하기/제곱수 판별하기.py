import math
def solution(n):
    answer =2
    m = math.sqrt(n)
    if int(m) == m:
        answer = 1
    return answer