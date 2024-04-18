import math
def solution(arr):
    answer = 0
    a = arr[0]
    for i in range(1,len(arr)):
        b = arr[i]
        a = (a*b)//math.gcd(a,b)
    return a