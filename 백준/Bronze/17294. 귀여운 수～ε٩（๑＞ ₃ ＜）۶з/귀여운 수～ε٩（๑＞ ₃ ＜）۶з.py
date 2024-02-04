import sys
n = sys.stdin.readline().strip()
if len(n) >= 3:
    temp = int(n[0]) - int(n[1])
    cnt = 0
    for i in range(len(n)-1):
        if temp != int(n[i]) - int(n[i+1]):
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            break
        else:
            cnt += 1
    if cnt == len(n) -1:
        print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")

else:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")