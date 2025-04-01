def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0] - 1
        j = com[1]
        k = com[2] - 1
        
        temp = array[i:j]
        temp.sort()
        answer.append(temp[k])
    return answer