class Solution {
    public boolean is_prime(int number) {
        if (number < 2) return false;
        for (int i=3; i<number; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
    
    public int solution(int[] nums) {
        int answer = 0;
        
        for (int i=0; i<nums.length; i++) {
            for (int j=i+1; j<nums.length; j++){
                for (int k=j+1; k<nums.length; k++) {
                    if (is_prime(nums[i] + nums[j] + nums[k])) answer += 1;
                }
            }
        }
        return answer;
    }
}