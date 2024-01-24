def solution(lottos, win_nums):
    key, cnt = lottos.count(0), 0
    temp = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    lottos.sort()
    lottos = lottos[key:]
    for num in lottos:
        if num in win_nums:
            cnt += 1
    return temp[cnt + key], temp[cnt]