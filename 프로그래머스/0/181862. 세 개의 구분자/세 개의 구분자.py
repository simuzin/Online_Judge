def solution(myStr):
    answer = []
    temp = myStr.replace('a', ' ')
    temp = temp.replace('b', ' ')
    temp = temp.replace('c', ' ')
    answer = temp.split()
    if not answer:
        answer.append("EMPTY")
    return answer