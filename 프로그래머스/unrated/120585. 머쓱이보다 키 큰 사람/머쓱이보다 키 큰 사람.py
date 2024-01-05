def solution(array, height):
    answer = 0
    for i in range(len(array)):
        if max(array) > height:
            array.pop()
            answer += 1
    return answer