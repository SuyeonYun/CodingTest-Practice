def solution(today, terms, privacies):
    today_y, today_m, today_d = map(int, today.split("."))
    
    result = []
    day_dict = {}
    terms_dict = {}
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    for i in range(1, 13):
        day_dict[i] = days[i]
    
    for t in terms:
        term, month = t.split(" ")
        terms_dict[term] = int(month)
    
    for i in range(len(privacies)):
        p = privacies[i]
        d, t = p.split(" ")
        y, m, d = map(int, d.split("."))
        
        m += int(terms_dict[t])
        y += int(m / 12)
        m %= 12
        
        if m == 0:
            y -= 1
            m = 12
        
        d -= 1
        if d == 0:
            m -= 1
            if m == 0:
                y -= 1
                m = 12
            d = day_dict[m]
        
        if today_y > y:
            result.append(i+1)
        elif today_y == y:
            if today_m > m:
                result.append(i+1)
            elif today_m == m:
                if today_d > d:
                    result.append(i+1)
                        
    return result
            
        
        
        
        
            