def solution(bandage, health, attacks):
    answer = health - attacks[0][1]
    temp = attacks[0][0]
    t,x,y = bandage[0], bandage[1], bandage[2]
    for time,attack in attacks[1:]:
        sigan = time - temp
        if sigan > 1:
            for i in range(1,sigan):
                if i % t == 0:
                    answer += y
                answer += x
                if answer >= health:
                    answer = health
                    break
        temp = time
        answer -= attack
        if answer <= 0:
            answer = -1
            break   
    return answer