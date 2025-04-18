def solution(citations):
    answer = 0
    cnt = len(citations)
    citations.sort(reverse = True);
    
    for i in range(citations[0]):
        if i <= cnt:
            answer = i
        if i in citations:
            cnt -= citations.count(i)
    return answer