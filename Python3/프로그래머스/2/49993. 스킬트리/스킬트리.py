def solution(skill, skill_trees):
    answer = 0
    
    for ex in skill_trees:
        temp = []
        for str in skill:
            idx = float('inf') if str not in ex else ex.find(str)
            temp.append(idx)
        if temp == sorted(temp):
            answer += 1
            
    return answer