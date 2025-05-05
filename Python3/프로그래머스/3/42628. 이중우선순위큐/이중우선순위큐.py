import heapq

def solution(operations):
    answer = [0, 0]
    queue = []
    
    for i in operations:
        op = i.split(" ")
        if op[0] == "I":
            queue.append(int(op[1]))
        else:
            if queue:
                if op[1] == "1":
                    queue.remove(max(queue))
                else:
                    queue.remove(min(queue))
    
    if queue:
        answer = [max(queue), min(queue)]
    return answer