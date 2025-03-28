import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int count = 0;
        int pos, temp;
        List<Integer> stack = new ArrayList<>();
        for (int i=0; i<moves.length; i++) {
            pos = moves[i] - 1;
            for (int j=0; j<board.length; j++) {
                if (board[j][pos] != 0) {
                    stack.add(board[j][pos]);
                    board[j][pos] = 0;
                    break;
                }
            }
            if (stack.size() >= 2 && 
                stack.get(stack.size() - 1) == stack.get(stack.size() - 2)) {
                stack.remove(stack.size() - 1);
                stack.remove(stack.size() - 1);
                count += 2;
            }
        }
        return count;
    }
}