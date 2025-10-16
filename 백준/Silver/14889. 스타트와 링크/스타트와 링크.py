import sys
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 팀의 인원
member_num = N // 2

# 팀 조합하기
temp = []
team = []
visited_team = [False] * N
def team_maker(start, depth):
    if depth == member_num:
        team.append(temp.copy())
        return
    for i in range(start, N):
        if visited_team[i] == False:
            visited_team[i] = True
            temp.append(i)
            team_maker(i + 1, depth + 1)
            visited_team[i] = False
            temp.pop()

# 팀 능력치 계산
def team_power(team):
    total = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                total += board[team[i]][team[j]]
    return total


team_maker(0, 0)
team_num = len(team) // 2

star_team = team[:team_num]
link_team = team[team_num:][::-1]
# print(star_team)
# print(link_team)

min_gap = 100
for num in range(team_num):
    # print(star_team[num])
    # print(link_team[num])
    # print("=======")
    star_power = team_power(star_team[num])
    link_power = team_power(link_team[num])

    min_gap = min(min_gap, abs(star_power - link_power))

print(min_gap)