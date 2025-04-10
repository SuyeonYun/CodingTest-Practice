def solution(skill, skill_trees):
    answer = 0
    
    for ex in skill_trees:
        temp = []
        for str in skill:
            idx = float('inf')
            if str in ex:
                idx = ex.find(str)
            temp.append(idx)
        print(f"temp:{temp}")
        print(f"sort temp:{sorted(temp)}\n")
        if temp == sorted(temp):
            answer += 1
    return answer