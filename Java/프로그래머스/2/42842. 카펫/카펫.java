class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int plus = (brown + 4) / 2;
        int mul = brown + yellow;
        
        for (int x=1; x<plus; x++) {
            int y = plus - x;
            if (x * y == mul) {
                answer[0] = y;
                answer[1] = x;
                return answer;
            }
        }
        return answer;
    }
}