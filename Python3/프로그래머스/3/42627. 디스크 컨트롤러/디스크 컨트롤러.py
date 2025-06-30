import heapq

def solution(jobs):
    q = []
    total = 0
    flag = False
    n = len(jobs)
    cur_time = -1
    remain_time = 0
    finish_task = 0
    max_time = max(jobs, key = lambda x:x[0])[0]
    
    tasks = [[] for _ in range(max_time + 1)]
    for idx in range(n):
        start, time = jobs[idx]
        tasks[start].append((idx, time))
    
    while finish_task < n:
        cur_time += 1
        if cur_time < max_time + 1 and tasks[cur_time]:
            for task in tasks[cur_time]:
                heapq.heappush(q, (task[1], cur_time, task[0]))
        
        if flag:
            remain_time -= 1
            if remain_time == 0:
                flag = False
                finish_task += 1
            else:
                continue
        
        if q:
            t, st, i = heapq.heappop(q)
            flag = True
            remain_time = t
            total += cur_time + t - st
        
    answer = total // n
    return answer
    