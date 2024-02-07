import sys
grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
score,total = 0,0
for _ in range(20):
    _,s,g = map(str,sys.stdin.readline().strip().split())
    if g == 'P':
        continue
    total += float(s)
    score += float(s)*grade[g]
print(score/total)