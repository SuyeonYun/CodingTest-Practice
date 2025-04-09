import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        int rest_weight = weight;
        List<Integer> bridge = new ArrayList<>();
        List<Integer> trucks = new ArrayList<>();
        for (int i=0; i<bridge_length; i++) bridge.add(0);
        for (int j=0; j<truck_weights.length; j++) trucks.add(truck_weights[j]);
        
        while(trucks.size() > 0) {
            time += 1;
            
            rest_weight -= bridge.get(bridge.size() - 1);
            rest_weight += bridge.get(0);
            
            bridge.remove(0);
            int temp = 0;
            if (rest_weight >= trucks.get(0)) temp = trucks.remove(0);
            bridge.add(temp);
        }
        return time + bridge_length;
    }
}   