n = int(input())
for i in range(n):
    s = input()
    answer, flag = [], 0
    for j in range(len(s)):
        if s[j] == 'O':
            flag += 1
        else:
            flag = 0
        answer.append(flag)
    print(sum(answer))