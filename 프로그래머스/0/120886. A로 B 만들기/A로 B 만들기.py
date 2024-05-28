def solution(before, after):
    answer = 0
    before_list = list(before)
    after_list = list(after)    
    before_list.sort()
    after_list.sort()
    
    if before_list == after_list:
        answer = 1
    return answer