def solution(progresses, speeds):
    days = []
    answer = []
    
    for p, s in zip(progresses, speeds):
        temp = (100 - p) % s
        if temp == 0:
            days.append((100 - p) // s)
        else:
            days.append((100 - p) // s + 1)
            
    while len(days) != 0:
        first = days.pop(0)
        count = 1
        for day in days:
            if day > first:
                break
            count += 1
        answer.append(count)
        if count > 1:
            for _ in range(1, count):
                days.pop(0)
    
    return answer
