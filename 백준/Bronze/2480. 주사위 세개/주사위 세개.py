import sys
dice = list(map(int, sys.stdin.readline().strip().split()))
if len(set(dice)) == 1:
    print(10000 + (dice[0])*1000)
elif len(set(dice)) == 2:
    a,b = set(dice)
    if dice.count(a) == 2:
        print(1000 + (a*100))
    else:
        print(1000 + (b*100))
else:
    print(max(dice)*100)