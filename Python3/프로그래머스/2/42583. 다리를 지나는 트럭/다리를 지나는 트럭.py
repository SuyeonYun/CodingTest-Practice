def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    rest_weight = weight
    
    while(len(truck_weights) != 0):
        time += 1
        rest_weight -= bridge[-1]
        rest_weight += bridge[0]
    
        cur_weight = 0
        if rest_weight >= truck_weights[0]:
            cur_weight = truck_weights.pop(0)
            
        bridge = bridge[1:]
        bridge.append(cur_weight)
        
    answer = time + bridge_length
    return answer

    