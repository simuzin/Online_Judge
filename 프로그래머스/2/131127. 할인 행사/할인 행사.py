from collections import Counter
def solution(want, number, discount):
    answer = 0
    want_dict = dict(zip(want,number))
    for i in range(len(discount)-10+1):
        temp = Counter(discount[i:i+10])
        flag = 0
        for product in want_dict:
            if want_dict[product] <= temp[product]:
                flag += 1
            else:
                break
        if flag == len(want):
            answer += 1
    return answer