def solution(arr):
    answer = [arr[0]]
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == prev:
            continue
        answer.append(arr[i])
        prev = arr[i]
    return answer