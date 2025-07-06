from collections import deque
import sys
sys.setrecursionlimit(20000)

class Node:
    def __init__(self, idx, price, child, parent, visited):
        self.idx = idx
        self.price = price
        self.child = child
        self.parent = parent
        self.visited = visited
    
    def __repr__(self):
        return repr((self.idx, self.price, self.child, self.parent, self.visited))

def solution(enroll, referral, seller, amount):
    l = len(enroll)
    q = deque()
    answer = []
    e_dict = {}
    employees = []
    
    e_dict["-"] = -1
    for i in range(l):
        e_dict[enroll[i]] = i
    
    for i in range(l):
        employees.append(Node(i, 0, [], e_dict[referral[i]], False))
        
    for i in range(l):
        if employees[i].parent >= 0:
            employees[employees[i].parent].child.append(i)
        
    for i in range(len(seller)):
        cur = employees[e_dict[seller[i]]]
        fee = amount[i] * 10
        cur.price += amount[i] * 90
        
        def dfs(c, f):
            if c.parent < 0 or f < 1:
                return f
            f1 = dfs(employees[c.parent], int(f * 0.1))
            employees[c.parent].price += (f - f1)
            return f
            
        dfs(cur, fee)
        
    for i in range(l):
        answer.append(employees[i].price)
        
    return answer
        