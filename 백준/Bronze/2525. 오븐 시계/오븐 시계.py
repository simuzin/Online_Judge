a,b = map(int, input().split())
c = int(input())

temp = (a * 60) + b + c
if temp >= 1440:
    temp %= 1440
h = temp // 60
m = temp % 60
print(h,m)