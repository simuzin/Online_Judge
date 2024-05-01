def solution(array):
    answer = 0
    for i in array:
        while True:
            if i%10 == 7:
                answer += 1
            i //= 10
            if i < 7:
                break
    return answer