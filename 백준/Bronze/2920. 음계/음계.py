pitch = list(map(int, input().split()))
flag = 0
for i in range(7):
    if pitch[i+1] - pitch[i] == 1:
        flag += 1
    elif pitch[i+1] - pitch[i] == -1:
        flag -= 1
if flag == 7:
    print("ascending")
elif flag == -7:
    print("descending")
else:
    print("mixed")