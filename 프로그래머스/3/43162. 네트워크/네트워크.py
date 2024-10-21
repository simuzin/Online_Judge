from collections import deque

def solution(n, computers):
    answer = 0
    visited_bfs = [False] * n
    
    def BFS (visited_bfs, computers, start_node):
            queue = deque([start_node]) 
            visited_bfs[start_node] = True
            while queue:
                node = queue.popleft()
                for i in range(n):
                    if computers[node][i] == 1 and not visited_bfs[i]:
                        queue.append(i)
                        visited_bfs[i] = True
                        
    for i in range(n):
        if not visited_bfs[i]:
            BFS(visited_bfs, computers, i)
            answer += 1
    return answer
        
        