def solution(money):
    jan = money // 5500
    change = money % 5500
    return jan, change