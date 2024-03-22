def solution(id_list, report, k):
    report = list(set(report))
    count = [0] * len(id_list)
    id_report = {}
    for report_info in report:
        user, reported_user = report_info.split()
        if user not in id_report:
            id_report[user] = []
        id_report[user].append(reported_user)
        count[id_list.index(reported_user)] += 1


    ban_id = []
    for i in range(len(count)):
        if count[i] >= k:
            ban_id.append(id_list[i])
    
    answer = []
    for user in id_list:
        cnt = 0
        if user in id_report:
            for ban in id_report[user]:
                if ban in ban_id:
                    cnt += 1
        answer.append(cnt)
    return answer