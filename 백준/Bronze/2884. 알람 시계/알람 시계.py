h,m = map(int, input().split())
temp = (h*60) + m - 45
if temp >= 0:
    print(temp // 60, temp % 60)
else:
    print("23",60+temp)