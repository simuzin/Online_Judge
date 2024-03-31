def solution(n):
    answer = 1
    pizza = 6
    while True:
        if pizza % n == 0:
            break
        answer += 1
        pizza += 6
    return answer