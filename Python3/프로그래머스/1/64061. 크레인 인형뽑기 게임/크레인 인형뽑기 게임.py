def solution(board, moves):
    count = 0
    stack = []
    for pos in moves:
        pos -= 1
        for row in board:
            if row[pos] != 0:
                stack.append(row[pos])
                row[pos] = 0
                break
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            count += 2
            
    return count