def solution(id_pw, db):
    answer = ''
    for user_id, user_pw in db:
        if id_pw[0] == user_id:
            if id_pw[1] == user_pw:
                answer = 'login'
            else:
                answer = 'wrong pw'
    if not answer:
        answer = 'fail'
    return answer