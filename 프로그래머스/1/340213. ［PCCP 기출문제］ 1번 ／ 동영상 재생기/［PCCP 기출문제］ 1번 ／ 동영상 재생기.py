def to_seconds(time):
    m, s = time.split(':')
    return int(m)*60 + int(s)

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    video_len_s = to_seconds(video_len)
    pos_s = to_seconds(pos)
    op_start_s = to_seconds(op_start)
    op_end_s = to_seconds(op_end)

    for command in commands:
        if op_start_s <= pos_s <= op_end_s:
            pos_s = op_end_s
            
        if command == 'prev':
            pos_s -= 10
            if pos_s < 0:
                pos_s = 0
        elif command == 'next':
            pos_s += 10
            if pos_s > video_len_s:
                pos_s = video_len_s
        
        if op_start_s <= pos_s <= op_end_s:
            pos_s = op_end_s

    answer = f'{pos_s // 60:02d}:{pos_s%60:02d}'
    return answer