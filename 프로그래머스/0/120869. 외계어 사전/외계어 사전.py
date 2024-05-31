def solution(spell, dic):
    answer = 2
    spell.sort()
    for word in dic:
        temp = list(set(list(word)))
        temp.sort()
        if temp == spell:
            answer = 1
            break
    return answer