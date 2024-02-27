alpha = [0]*26
s = input()
for a in s:
    alpha[ord(a) - ord('a')] += 1
print(*alpha)