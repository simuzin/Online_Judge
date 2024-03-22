def solution(my_string):
    answer = [0] * 26 * 2
    for i in my_string:
        if i.isupper() == 1:
            answer[ord(i)-ord('A')] += 1
        else:
            answer[ord(i)-ord('a') + 26] += 1
    return answer