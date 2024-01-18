def solution(citations):
    citations.sort(reverse =True)
    h_index = 0
    for i, cite in enumerate(citations):
        if cite >= i+1:
            h_index = i+1
            print(cite, i+1, h_index)
        else:
            break
    return h_index
        
        