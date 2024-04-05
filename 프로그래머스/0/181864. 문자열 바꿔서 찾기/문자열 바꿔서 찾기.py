def solution(myString, pat):
    answer = 0
    key = pat.replace('A','1')
    key = key.replace('B','0')
    key = key.replace('1','B')
    key = key.replace('0','A')
    if key in myString:
        answer = 1
    return answer