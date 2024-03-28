import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while True:
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            count = -1
            break
        first_low = heapq.heappop(scoville)
        second_low = heapq.heappop(scoville)
        heapq.heappush(scoville, first_low + (second_low*2))
        count += 1
    return count