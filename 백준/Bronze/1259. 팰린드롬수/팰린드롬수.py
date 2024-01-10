while True:
    s = input()
    if int(s) == 0:
        break
    if s == s[::-1]:
        print("yes")
    else:
        print("no")