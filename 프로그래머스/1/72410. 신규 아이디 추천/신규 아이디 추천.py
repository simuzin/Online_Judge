def solution(new_id):
    answer = ''
    temp = []
    for i, c in enumerate(new_id.lower()):
        if '0'<=c<='9' or 'a'<=c<='z' or c == '-' or c == '_' or c == '.':
            temp.append(c)
            if temp[-2:] == ['.','.']:
                temp.pop()
    new = ''.join(str(i) for i in temp).strip('.')
    answer = new[:15].strip('.')
    if len(answer) == 0:
        answer  = 'a'
    if len(answer) <= 2:
        while True:
            if len(answer) == 3:
                break
            answer += answer[-1]
    return answer