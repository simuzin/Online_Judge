def solution(today, terms, privacies):
    answer = []
    
    y,m,d = today.split('.')
    trans_today = (int(y)-2000)*12*28 + int(m)*28 + int(d)

    # 약관 정리
    type_info = {}
    for info in terms:
        type, month =info.split()
        type_info[type] = int(month)
    
    # 개인 정보 수집 일자 비교
    for i, info in enumerate(privacies):
        day, type = info.split()

        yy, mm, dd = day.split('.')
        trans_day =(int(yy)-2000)*12*28 + int(mm)*28 + int(dd) + (type_info[type] * 28) - 1

        if trans_day < trans_today:
            answer.append(i+1)
            
    return answer