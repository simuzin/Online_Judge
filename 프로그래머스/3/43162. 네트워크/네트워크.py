from collections import deque

def solution(n, computers):
    answer = 0
    visited_bfs = [False] * n
    
    for i in range(n):
        # BFS 구현하기 (그래프)
        if not visited_bfs[i]:
            queue = deque([i]) 
            visited_bfs[i] = True
            answer += 1
            while queue:
                node = queue.popleft()
                for j in range(n):
                    if computers[node][j] == 1 and not visited_bfs[j]:
                        queue.append(j)
                        visited_bfs[j] = True
    return answer
        
        