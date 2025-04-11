def solution(priorities, location):
    queue = []
    pos = []
    
    for i in range(len(priorities)):
        queue.append(i)
        
    while len(queue) > 0:
        max_idx = max(priorities)
        cur_idx = queue.pop(0)
        if priorities[cur_idx] < max_idx:
            queue.append(cur_idx)
            continue
        pos.append(cur_idx)
        priorities[cur_idx] = -1
        
    return pos.index(location) + 1
    