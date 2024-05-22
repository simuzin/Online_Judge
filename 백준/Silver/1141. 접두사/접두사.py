import sys
n = int(sys.stdin.readline().strip())
words, count = [], 0
for _ in range(n):
    word = sys.stdin.readline().strip()
    words.append(word)
words.sort()
for i in range(n):
    for j in range(i+1,n):
        if words[j].startswith(words[i]):
            count += 1
            break
print(n-count)