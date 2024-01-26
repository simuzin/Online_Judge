import sys
aeiou = ['a','e','i','o','u']
while True:
    s = sys.stdin.readline().strip().lower()
    if s == '#':
        break
    cnt = 0
    for c in s:
        if c in aeiou:
            cnt += 1
    print(cnt)