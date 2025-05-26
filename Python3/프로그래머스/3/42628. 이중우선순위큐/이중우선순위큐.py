import heapq

def solution(operations):
    answer = [0, 0]
    arr = []
    
    for o in operations:
        oper, num = o.split(" ")
        if oper == "I":
            heapq.heappush(arr, int(num))
        elif oper == "D" and arr:
            if num == "-1":
                heapq.heappop(arr)
            else:
                arr.remove(max(arr))
    
    if arr:
        return [max(arr), arr[0]]
    return answer
            