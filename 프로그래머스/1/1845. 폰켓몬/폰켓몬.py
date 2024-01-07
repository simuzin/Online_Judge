def solution(nums):
    answer = len(set(nums))
    select = len(nums)//2
    if answer <= select:
        return answer
    else:
        return select