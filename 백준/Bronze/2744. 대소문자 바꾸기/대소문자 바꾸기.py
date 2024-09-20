import sys
s = sys.stdin.readline()
res=''
for c in s:
    if c.islower() == 0:
        res += c.lower()
    else:
        res += c.upper()
print(res)