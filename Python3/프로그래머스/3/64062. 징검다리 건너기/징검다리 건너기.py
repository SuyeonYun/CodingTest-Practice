class Node:
    def __init__(self, Prev, Cur, Next):
        self.Prev = Prev
        self.Cur = Cur
        self.Next = Next
    def __repr__(self):
        return repr((self.Prev, self.Cur, self.Next))

def solution(stones, k):
    answer = 0
    stone_obj = []
    for i in range(len(stones)):
        stone_obj.append(Node(i - 1, i, i + 1))
    
    for idx in sorted(range(len(stones)), key = lambda i: stones[i]):
        answer = stones[idx]
        left, right = stone_obj[idx].Prev, stone_obj[idx].Next
        
        if left >= 0:
            stone_obj[left].Next = right
        if right < len(stones):
            stone_obj[right].Prev = left
        if right - left > k:
            return answer
    
    return answer
        