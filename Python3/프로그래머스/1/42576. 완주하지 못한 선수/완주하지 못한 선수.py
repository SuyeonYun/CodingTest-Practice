def solution(participant, completion):
    part_dict = {}
    for p in participant:
        if p in part_dict:
            part_dict[p] += 1
        else:
            part_dict[p] = 1
            
    for c in completion:
        part_dict[c] -= 1
    
    for ret in part_dict.keys():
        if part_dict[ret] > 0:
            return ret