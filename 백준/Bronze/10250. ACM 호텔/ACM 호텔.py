t = int(input())
for i in range(t):
    h,w,n = map(int, input().split())
    xx = (n // h) + 1
    yy = (n % h)
    if yy == 0:
        xx -= 1
        yy = h
    if xx < 10:
        print(f'{yy}0{xx}')
    else:
        print(f'{yy}{xx}')