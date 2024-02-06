import sys
s = sys.stdin.readline().strip()
cro_alpha = ['c=','c-','d-','lj','nj','s=','z=']
temp = ''
for c in s:
    temp += c
    if temp[-3:] == 'dz=':
        temp = temp[:-3] + '*'
    elif temp[-2:] in cro_alpha:
        temp = temp[:-2] + '*'
print(len(temp))