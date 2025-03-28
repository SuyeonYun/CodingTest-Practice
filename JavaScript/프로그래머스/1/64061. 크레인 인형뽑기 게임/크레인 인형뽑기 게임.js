function solution(board, moves) {
    var stack = [];
    var count = 0;
    for (let i=0; i<moves.length; i++) {
        let pos = moves[i]-1;
        for (let j=0; j<board.length; j++){
            if (board[j][pos] != 0) {
                stack.push(board[j][pos]);
                board[j][pos] = 0;
                break;
            }
        }
        if (stack.length >= 2 && stack[stack.length - 1] == stack[stack.length - 2]) {
            stack.pop();
            stack.pop();
            count += 2;
        }
    }
    return count;
}