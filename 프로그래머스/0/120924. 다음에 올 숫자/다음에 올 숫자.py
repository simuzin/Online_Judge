def solution(common):
    answer = 0
    temp = []
    for i in range(1,len(common)):
        temp.append(common[i] - common[i-1])
    choose = temp[-1] - temp[-2]
    if choose:
        ratio = common[1] // common[0]
        answer = common[-1] * ratio
    else:
        answer = common[-1] + temp[0]
    return answer