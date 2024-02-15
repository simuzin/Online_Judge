import sys
s = sys.stdin.readline().strip()
s_dict = []
for i in range(len(s)):
    s_dict.append(s[i:])
for w in sorted(s_dict):
    print(w)