def solution(str_list):
    answer = []
    if "l" in str_list or 'r' in str_list:
        for i,c in enumerate(str_list):
            answer.append(c)
            if c == 'l':
                answer.pop()
                break
            elif c == 'r':
                answer = str_list[i+1:]
                break
    return answer