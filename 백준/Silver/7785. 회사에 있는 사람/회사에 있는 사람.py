import sys
n = int(sys.stdin.readline().strip())
company = {}
for _ in range(n):
    name, state = map(str, sys.stdin.readline().strip().split())
    company[name] = state
company = [n for n,s in company.items() if s == 'enter']
company.sort(reverse = True)
for name in company:
    print(name)