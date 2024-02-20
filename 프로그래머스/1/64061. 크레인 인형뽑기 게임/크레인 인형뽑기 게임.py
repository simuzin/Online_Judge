def solution(board, moves):
    answer = 0
    temp, stack = [], []
    for j in range(len(board[0])):
        temp.append([])
        for i in range(len(board)):
            if board[i][j] != 0:
                temp[-1].append(board[i][j])
    for i in moves:
        if temp[i-1]:
            stack.append(temp[i-1].pop(0))
            if (len(stack) >= 2) and (stack[-2] == stack[-1]):
                stack.pop()
                stack.pop()
                answer += 2   
    return answer