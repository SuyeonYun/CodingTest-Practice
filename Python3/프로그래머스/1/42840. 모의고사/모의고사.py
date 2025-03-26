def solution(answers):
    answer = []
    count = [-1,0,0,0]
    ans_1 = [1, 2, 3, 4, 5]
    ans_2 = [ 2, 1, 2, 3, 2, 4, 2, 5]
    ans_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == ans_1[i % len(ans_1)]:
            count[1] += 1
        if answers[i] == ans_2[i % len(ans_2)]:
            count[2] += 1
        if answers[i] == ans_3[i % len(ans_3)]:
            count[3] += 1
            
    max_num = max(count)
    for j in range(len(count)) :
        if count[j] == max_num:
            answer.append(j)
    return answer