import sys

h, m, s = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())


temp = h * 60 * 60 + m * 60 + s + d
hh, mm = 0, 0
while temp >= 60 * 60:
    temp -= 60 * 60
    hh += 1
while temp >= 60:
    temp -= 60
    mm += 1

print(hh % 24 , mm, temp)