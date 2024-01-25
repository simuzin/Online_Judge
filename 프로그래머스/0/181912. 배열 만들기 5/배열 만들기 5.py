def solution(intStrs, k, s, l):
    answer = []
    for num in intStrs:
        temp = num[s:s+l]
        if int(temp) > k:
            answer.append(int(temp))
    return answer