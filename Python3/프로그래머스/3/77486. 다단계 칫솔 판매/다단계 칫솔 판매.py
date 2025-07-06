from collections import deque

class Node:
    def __init__(self, idx, price, parent):
        self.idx = idx
        self.price = price
        self.parent = parent
    
    def __repr__(self):
        return repr((self.idx, self.price, self.parent))

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
        employees.append(Node(i, 0, e_dict[referral[i]]))
        
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
        