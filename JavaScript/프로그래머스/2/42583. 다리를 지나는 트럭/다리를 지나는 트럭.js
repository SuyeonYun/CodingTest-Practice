function solution(bridge_length, weight, truck_weights) {
    var bridge = Array(bridge_length).fill(0);
    var time = 0;
    var rest_weight = weight;
    
    while (truck_weights.length > 0) {
        time += 1;
        
        rest_weight -= bridge[bridge.length - 1];
        rest_weight += bridge[0];
        
        bridge.shift();
        
        let temp = 0;
        if (rest_weight >= truck_weights[0]) {
            temp = truck_weights.shift();
        }
        bridge.push(temp);   
    }
    return time + bridge_length;
}