def solution(wallpaper):
    w,h = [],[]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                h.append(j)
                w.append(i)
    return [min(w), min(h), max(w)+1, max(h)+1]