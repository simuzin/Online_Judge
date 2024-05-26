def solution(chicken):
    coupons = chicken // 10
    rest = (chicken % 10) + (chicken // 10)
    while rest >= 10:
        coupons += rest // 10
        rest = (rest % 10) + (rest // 10)
    return coupons