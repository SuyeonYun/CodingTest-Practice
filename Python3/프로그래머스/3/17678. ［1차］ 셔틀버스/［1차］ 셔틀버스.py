def solution(n, t, m, timetable):
    answer = 0
    start = 540
    last_bus = 540 + (n - 1) * t
    
    crew = {}
    remain_crew = []
    
    timetable.sort()
    for i in timetable:
        hour, minute = map(int, i.split(":"))
        time = 60 * hour + minute
        if last_bus < time < 1440:
            continue
        crew[time] = crew.setdefault(time, 0) + 1
        
    cur = start
    for _ in range(n - 1):
        for _ in range(m):
            for key in crew.keys():
                if key <= cur :
                    if crew[key] > 0:
                        crew[key] -= 1
                        break
        cur += t

    for key in crew.keys():
        for item in range(crew[key]):
            remain_crew.append(key)
            
    if len(remain_crew) < m:
        answer = last_bus
        
    else:
        while len(remain_crew) >= m:
            answer = remain_crew[-1]
            cnt = remain_crew.count(answer)
            for _ in range(cnt):
                remain_crew.pop(-1)                
        answer -= 1

    hour = answer // 60
    minute = answer % 60
    return f"{hour:02d}:{minute:02d}"
    